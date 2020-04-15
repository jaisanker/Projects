library(tm)
library(scales)
library(plotly)
library(igraph)
library(ggraph)
library(tidytext)
library(pdftools)
library(reshape2)
library(tidyverse)
library(textreadr)
library(wordcloud)

setwd("/Users/jaisankerv/Downloads/02 Individual Assignment/Data")
x <- list.files(path="/Users/jaisankerv/Downloads/02 Individual Assignment/Data", pattern = "pdf$")

opi <- lapply(x, pdf_text)

lapply(opi, length) 
corps <- Corpus(URISource(x),readerControl = list(reader = readPDF))
my_df <- tidy(corps)

junk_common<-data_frame(word=c("donald","trump","president","applause","people","country","american", "americans","america", 
                                "united","god", "bless", "laughter","lot","ahead","called","talking","dollars","day","time",
                                "happen","ago","love","tremendous","citizens","billion","usa",
                                "sanders", "senator", "sen", "margaret", "bernie", "campaign", "chris","cuomo", "question","brennan","hayes"),
                                lexicon="junk")
my_df_tokens <- my_df %>%
  group_by(id)%>%
  unnest_tokens(word, text) %>%
  anti_join(stop_words)%>%
  anti_join(junk_common)%>%
  anti_join(stop_words) %>%
  filter(
    !str_detect(word, pattern = "[[:digit:]]"), # removes any words with numeric digits
    !str_detect(word, pattern = "[[:punct:]]"), # removes any remaining punctuations
    !str_detect(word, pattern = "\\b(.)\\b")    # removes any remaining single letter words
  ) %>%
  count(word,sort=TRUE)

trump_tokens<-my_df_tokens%>%
  filter(id=="Trump.pdf")
bernie_tokens<-my_df_tokens%>%
  filter(id=="Bernie.pdf")

#------------------------------FREQUENCY-----------------------------------------------
ggplot(trump_tokens %>% filter(n >= 50), aes(x=reorder(word,n), y=n))+ 
  geom_col() + coord_flip() + ggtitle("Donald Trump")+
  geom_bar(stat = "identity", alpha = 0.7,fill = "#E91D0E") + #republican red #E91D0E
  theme_minimal(base_size = 14) +
  theme(panel.grid.major.y = element_blank(),
        panel.grid.minor.y = element_blank()) +
  ylab("frequency") +
  xlab("words") 

ggplot(bernie_tokens %>% filter(n >= 40), aes(x=reorder(word,n), y=n))+ 
  geom_col() + coord_flip() + ggtitle("Bernie Sanders")+
  geom_bar(stat = "identity", alpha = 0.7,fill = "#0015BC") + #democratic blue #0015BC
  theme_minimal(base_size = 14) +
  theme(panel.grid.major.y = element_blank(),
        panel.grid.minor.y = element_blank()) +
  ylab("frequency") +
  xlab("words") 

#-------------------------------------------AFINN SENTIMENT-----------------------------------------
trump_tokens %>% inner_join(get_sentiments("afinn")) %>% mutate((total= value * n)) %>% summarise(sum=sum(value))
bernie_tokens %>% inner_join(get_sentiments("afinn")) %>% mutate((total= value * n)) %>% summarise(sum=sum(value))
#---------------------------------------BING SENTIMENT-----------------------------------------------
trump_sentiments<-trump_tokens %>%
  inner_join(get_sentiments("bing"))%>%
  count(word,sentiment)%>%
  count(sentiment)

bernie_sentiments<-bernie_tokens %>%
  inner_join(get_sentiments("bing"))%>%
  count(word,sentiment)%>%
  count(sentiment)

trump_sentiments
bernie_sentiments
#-------------------------------------------------SENTIMENT WORD CLOUD---------------------------------------------- 

my_df_tokens_sentiments <- my_df %>%
  unnest_tokens(word, text) %>%
  anti_join(stop_words)%>%
  anti_join(junk_common)%>%
  inner_join(get_sentiments("nrc")) %>%
  count(word,sentiment)%>%
  count(sentiment)
my_df_tokens_sentiments

my_df_tokens_sentiments %>%
  inner_join(get_sentiments("nrc")) %>%
  count(word, sentiment, sort=TRUE) %>%
  acast(word ~sentiment, value.var="n", fill=0) %>%
  comparison.cloud(colors = c("grey20", "gray80"),
                   max.words=100, fixed.asp=TRUE, scale=c(0.8,0.8), title.size=1, rot.per=0.25)
#-------------------------------------------------BI-GRAMS---------------------------------------------- 
bi_grams <- my_df %>% 
  unnest_tokens(bigram, text, token = "ngrams", n = 2) %>%
  separate(bigram, into = c("first","second"), sep = " ", remove = FALSE) %>% # remove stop words from tidytext package 
  anti_join(stop_words, by = c("first" = "word")) %>%
  anti_join(junk_common, by = c("first" = "word")) %>%
  anti_join(stop_words, by = c("second" = "word")) %>%
  anti_join(junk_common, by = c("second" = "word")) %>%
  filter(str_detect(first, "[a-z]"),
         str_detect(second, "[a-z]")) %>%
  group_by(id) %>%
  count(bigram) %>%
  arrange(-n)
bi_grams_trump <- bi_grams%>%
  filter(id=="Trump.pdf")
bi_grams_bernie <- bi_grams%>%
  filter(id=="Bernie.pdf")

bi_grams_trump
bi_grams_bernie

#Cleaning
top_bigram_f$id <- gsub("Trump.pdf","Donald Trump", top_bigram_f$id)
top_bigram_f$id <- gsub("Bernie.pdf","Bernie Sanders", top_bigram_f$id)


bigram_f$id <- gsub("Trump.pdf","Donald Trump", bigram_f$id)
bigram_f$id <- gsub("Bernie.pdf","Bernie Sanders", bigram_f$id)

bigram_graph <- bigram_f %>%
  filter(n>7) %>%
  graph_from_data_frame() 
bigram_graph
ggraph(bigram_graph, layout = "fr") +
  geom_edge_link()+
  geom_node_point()+
  geom_node_text(aes(label=name), vjust =1, hjust=1)

#--------------tf-idf for bigram--------------------------------------------------------------------------
#couldn't derive any meaning ful insights
bigram_tf_idf <- bi_grams %>%
  count(id, bigram) %>%
  bind_tf_idf(bigram, id, n) %>%
  arrange(desc(tf_idf))

bigram_tf_idf
bigram_tf_idf_trump<-bigram_tf_idf%>%
  filter(id=="Trump.pdf")

bigram_tf_idf_bernie<-bigram_tf_idf%>%
  filter(id=="Bernie.pdf")

#--------------tf-idf--------------------------------------------------------------------------
original_df <- my_df %>%
  unnest_tokens(word, text) %>%
  anti_join(stop_words) %>%
  anti_join(junk_common) %>%
  count(id, word, sort=TRUE) %>%
  ungroup() 
total_words <- original_df %>%
  group_by(id) %>%
  summarize(total=sum(n)) 
original_df_words <- left_join(original_df, total_words) 
original_df_words <- original_df_words %>%
  bind_tf_idf(word, id, n) 

original_df_words %>%
  arrange(desc(tf_idf))

original_df_words$id <- gsub("Trump.pdf","Donald Trump", original_df_words$id)
original_df_words$id <- gsub("Bernie.pdf","Bernie Sanders", original_df_words$id)

original_df_words %>%
  arrange(desc(tf_idf)) %>%
  mutate(word=factor(word, levels=rev(unique(word)))) %>%
  group_by(id) %>%
  top_n(30) %>%
  ungroup %>%
  ggplot(aes(word, tf_idf, fill=id))+
  geom_col(show.legend=FALSE)+
  labs(x=NULL, y="tf-idf")+
  theme_minimal(base_size = 14) +
  theme(panel.grid.major.y = element_blank(),
        panel.grid.minor.y = element_blank()) +
  facet_wrap(~id, ncol=2, scales="free")+
  coord_flip()

