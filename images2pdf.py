import os
import img2pdf

def jpgs2pdf(output_pdf, input_images_folder):
    try:
        with open(output_pdf, "wb") as f:
            f.write(
                img2pdf.convert(
                    [input_images_folder + '/' + i for i in os.listdir(input_images_folder) if i.endswith(".png") or i.endswith(".jpg")]
                                )
                    )
    except Exception as err:
        print(err)
        raise


if __name__ == '__main__':

    output_pdf = 'C:\\Project\\images2pdf\\Starter_Pokemon_Generation_1.pdf'
    input_images_folder = 'C:\\Project\\images2pdf\\images'
    
    jpgs2pdf(output_pdf, input_images_folder)
    os.startfile(output_pdf)
