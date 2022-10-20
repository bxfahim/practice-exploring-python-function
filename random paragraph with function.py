# """
# Huawei is a leading global provider of information and communications technology (ICT) infrastructure and smart devices.
# It designs, develops, produces and sells telecommunications equipment.
#
# The Huawei ban prevents Huawei from working with US-based companies in the creation of its products.
# It's not illegal to own a Huawei device anywhere in the world.
#
# It doesn't apply to consumers who currently own a Huawei product and doesn't prevent them from buying new ones, either.
#
# """
from random import choice
sentence_one = [
    "Huawei is a top global supplier of smart products and ICT (information and communications technology) infrastructure.",
    "Huawei is one of the top manufacturers of smart gadgets and ICT (information and communications technology) infrastructure in the world.",
    "ICT (information and communications technology) infrastructure and smart gadgets are two things that Huawei is a top provider of globally.",
    "Huawei is a leading global provider of information and communications technology (ICT) infrastructure and smart devices. It designs, develops, produces and sells telecommunications equipment.",
]

sentence_two = [
    "he Huawei ban prevents Huawei from working with US-based companies in the creation of its products. It's not illegal to own a Huawei device anywhere in the world.",
    "The Huawei prohibition restricts Huawei from collaborating on product development with US-based businesses.",
    "The Huawei prohibition restricts Huawei from collaborating with US-based businesses to develop its goods. Anywhere in the world, owning a Huawei device is legal.",
    "Huawei is forbidden from collaborating on product development with US-based businesses.",
]

sentence_three = [
    "It doesn't apply to consumers who currently own a Huawei product and doesn't prevent them from buying new ones, either.",
    "Customers who already own a Huawei product are not subject to it, and it does not hinder them from purchasing new ones.",
    "Customers who currently own a Huawei product are exempt from it, and it does not prevent them from purchasing new ones either.",
    "It doesn't apply to customers who already own a Huawei product and it doesn't stop them from purchasing new ones.",
]

# random selection from sentences
# concatination of all sentences
# add html p tag

def paragraph_formation(s1,s2,s3):
    """
    This function will create random paragraph
    :param s1,s2,s3: list of sentences
    :return: A paragraph
    """
    paragraph = choice(s1) + choice(s2) + choice(s3)
    return f'<p>{paragraph}</p>'

print(paragraph_formation(sentence_one, sentence_three, sentence_two))
print(paragraph_formation(sentence_one, sentence_three, sentence_two))
print(paragraph_formation(sentence_one, sentence_three, sentence_two))