paragraph1 = "This is paragraph one"
paragraph2 = "This is paragraph two"
paragraph3 = "This is paragraph three"
paragraph4 = "This is paragraph four"
#
# paragraph1_html = f'<p> {paragraph1} </p>'
# paragraph2_html = f'<p> {paragraph2} </p>'
# paragraph3_html = f'<p> {paragraph3} </p>'
# paragraph4_html = f'<p> {paragraph4} </p>'



def paragraph_html(paragraph):
    paragraph_html = f'<p> {paragraph} </p>'
    return paragraph_html

paragraph1_html = paragraph_html(paragraph1)
paragraph2_html = paragraph_html(paragraph2)
paragraph3_html = paragraph_html(paragraph3)
paragraph4_html = paragraph_html(paragraph4)

print(paragraph2_html)

def h2_html(text):
    h2 = f'<h2> {text.title()} </h2>'
    return h2

print(h2_html('Top 10 produt reviews'))
