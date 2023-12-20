#!/usr/bin/python
import os
from art import *
from argparse import ArgumentParser

# function to define help and take arguemnts 
def take_args():
    parser = ArgumentParser(
        prog='TEXT TO ASCII ART', 
        description="example: genascii -s/--string Hello World -f/--font black", 
        epilog="Please dont use space between arguments. Thank you for supporting.")
    # Adding text argument
    parser.add_argument(
        '-s',
        '--string', 
        type=str, 
        help="text", 
        required=True)
    # Adding font argument
    parser.add_argument(
        '-f',
        '--font', 
        type=str, 
        help="font you want to use", 
        default="random")
    # Adding ouput argument
    parser.add_argument(
        '-o',
        '--output', 
        type=str, 
        help="specify a file to output the result.")
    
    # Take arguments
    args = parser.parse_args()
    text = args.string
    font = args.font
    output = args.output
    return text, font, output

# function to generate art
def generateArt(text, font, output):
    # convert the text to art
    art = text2art(text, font)
    # if output is there then save it in a file
    if output:
        with open(os.path.join(os.curdir, output), "w") as f:
            f.write(art)
            f.close()
    # otherwise print on the console.
    else:
        tprint("TEXT TO ASCII ART", "small")
        print(art)

# main function to call everything together
def main ():
    text, font, output = take_args()
    generateArt(text, font, output)
    
if __name__ == "__main__":
    main()
