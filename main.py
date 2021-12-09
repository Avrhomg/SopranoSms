import requests
import argparse
from lxml import etree

if __name__ == '__main__':
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('U', type=str, action='store', help='Enter the account user name')
    my_parser.add_argument('P', type=str, action='store', help='Enter the account password')
    my_parser.add_argument('i_0', type=str, action='store', help='Enter the 1st phone Number To Send the SMS')
    my_parser.add_argument('i_1', type=str, action='store', help='Enter the 2nd phone Number To Send the SMS')
    my_parser.add_argument('i_2', type=str, action='store', help='Enter the 3rd phone Number To Send the SMS')
    my_parser.add_argument('i_3', type=str, action='store', help='Enter the 4th phone Number To Send the SMS')
    my_parser.add_argument('i_4', type=str, action='store', help='Enter the 5th phone Number To Send the SMS')
    my_parser.add_argument('k', type=str, action='store', help='Enter the senders phone number')
    my_parser.add_argument('data', type=str, action='store', help='Enter the text for SMS')
    my_parser.add_argument('e', type=str, action='store', help='Enter Service Password')
    args = my_parser.parse_args()
    username = args.U
    password = args.P
    phone_0 = args.i_0
    phone_1 = args.i_1
    phone_2 = args.i_2
    phone_3 = args.i_3
    phone_4 = args.i_4
    reply = args.k
    data = args.data
    #print(args.U, args.P, args.i, args.k, args.data)
    if args.e == 'afcon@2021':
        # Create the root element
        page = etree.Element('sms')

        # Make a new document tree
        doc = etree.ElementTree(page)

        # Add the subelements
        pageElement1 = etree.SubElement(page, 'account')
        subelement2 = etree.SubElement(pageElement1, 'id').text = username
        subelement3 = etree.SubElement(pageElement1, 'password').text = password

        # Add the subelements for "Attributes" tree
        pageElement2 = etree.SubElement(page, 'attributes')
        subelement4 = etree.SubElement(pageElement2, 'reference').text = '123'
        subelement5 = etree.SubElement(pageElement2, 'replyPath').text = reply

        # Add the subelements for "schedule" tree
        pageElement3 = etree.SubElement(page, 'schedule')
        subelement6 = etree.SubElement(pageElement3, 'relative').text = '0'

        # Add the subelements for "targets" tree
        pageElement4 = etree.SubElement(page, 'targets')
        subelement7 = etree.SubElement(pageElement4, 'cellphone', reference='0').text = phone_0
        subelement7_1 = etree.SubElement(pageElement4, 'cellphone', reference='1').text = phone_1
        subelement7_2 = etree.SubElement(pageElement4, 'cellphone', reference='2').text = phone_2
        subelement7_3 = etree.SubElement(pageElement4, 'cellphone', reference='3').text = phone_3
        subelement7_4 = etree.SubElement(pageElement4, 'cellphone', reference='4').text = phone_4
        # Add the subelements for "data" tree
        pageElement5 = etree.SubElement(page, 'data').text = data


        # Save to XML file
        doc.write('output.xml', pretty_print=True, xml_declaration=True, encoding='ISO-8859-1')



 #Set the path of the XML file.
xml_file = "output.xml"


# Open the XML file.
with open(xml_file) as xml:
    # Give the object representing the XML file to requests.post.
    r = requests.post('https://secureapi.soprano.co.il', data=xml)

# Write submission report into a txt file
print(r.content)
file1 = open("c:/soprano_submission_report.txt", "ab")
file1.write(r.content)
