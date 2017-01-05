# 클래스 class

#####Article variables

# title1 = "개발"
# author1 = "마르코"
# content1 = "개발은 쉬워요"
# view_count1 = 0
#
# title2 = "코칭"
# author2 = "마르코"
# content2 = "코칭은 쉬워요"
# view_count1 = 0
#
# title3 = "창업"
# author3 = "마르코"
# content3 = "창업은 쉬워요"
# view_count3 = 0

##### Article class
#class starts with Capital
# class Article:
#     title = "개발"
#     author = "마르코"
#     content = "개발은 쉬워요"
#     view_count = 0
#
# article1 = Article()
# print(article1.title)
#
# article2 = Article()
# article2.title="Coaching"
# print("변경후")
# print(article1.title)
# print(article2.title)




##### Article class with __init
class Article:
    author = "Marco"
    view_count = 0

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def read(self):
        self.view_count = self.view_count+1

article1 = Article("dev","dev is easy")
article2 = Article("coaching", "coaching is easy")
article3 = Article("start-up","start-up is easy")

#
# print(article1.view_count)
# # print(article2)
# # print(article3)
#
# article1.read()
# print(article1.view_count)



##### Article class inheritance 상속
class BrunchArticle(Article):
        # author = "Marco"
        # view_count = 0
        source = "Brunch"
        def read(self):
            self.view_count = self.view_count + 2
        # def __init__(self, title, content):
        #     self.title = title
        #     self.content = content
        #
        # def read(self):
        #     self.view_count = self.view_count+1

brunch_article = BrunchArticle("Dev", "Dev is easy")
print(brunch_article.view_count)

brunch_article.read()
print(brunch_article.view_count)
