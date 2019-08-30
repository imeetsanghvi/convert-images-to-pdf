# convert-images-to-pdf
Hello, this is a basic tutorial on how to convert multiple images into a single pdf output file  

Requirements:  img2pdf  
find it here: https://pypi.org/project/img2pdf/  

The steps are easy and as follows:  
1.	Choose the path of your images that you want to convert  
2.	Give the path to output pdf file with its name where you want to store the pdf file  
3.	Run the code  

Explanation: 
Inside if main: 
1.	Line 19 & 20 – are path to the output_pdf file and input_image_folder respectively 
2.	We pass both the path to the imgs2pdf function 
3.	Inside imgs2pdf function 		
4.  In line 6 - we open the pdf file as write byte(if file exists, it opens the file else it creates a new file with the name provided) 	
5.  In line 7 - we write to the file the images 		
6.  In line 8 and 9 - we get all the images which have extension ‘.jpg’ or ‘.png’ from the folder path using os.listdir   


Output:
This creates a pdf file in the path provided with all the jpg and png images into a single pdf file
