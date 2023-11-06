# >>Data Compression
# Reasons: 1) storage space, 2) transmission speed
# Like abbreviations: use the least number of bits possible to express something

#     Examples:
#     XXXOOXX --> X^3 O^2 X^2

#     I attend Pasadena High School. At Pasadena High Schoo, I am in the App Academy
#     --> I attend PHS. At PHS, I am in the App Academy

#     May use characters to represent things: use a dictionary
#     EX (Humpty Dumpty nursery rhyme):
#         sun --> umpty
#         fan --> all
#         star --> H sun D sun (humpty dumpty)
#         umbrella --> fan the king's (all the king's)


# >>Image Compression
#     All the pixels from here to here and here to here are "insert color"
#     Find an area with color repeats and representing that rather than the indiv pixels
#         OR 
#     Find the average "insert color" in an area and color that area all the same

# >>Compressing Difficult Data: 
#     AUDIO - find what we can cut out (while maining the same message)
#         - cut out the too low and too frequencies (that we can't hear anyway)
#         - cut out all the background noise stuff
#         - reduces the size of the file

# >>Lossless Compression: reduces the number of bits stored or transmitted while guaranteeing complete reconstruction of the data
#     Uses - executable files, text, spreadsheet files
#     Compresses less than lossy

# >>Lossy Compression: significantly reduces the number of bits stored or transmitted 
#                     but only allows reconstruction of an approximation of the data
#     Uses - graphics, audio, video, images
#     Compresses a lot more