import face_recognition
import os
import shutil

# Define the path to the server folder containing images to search
server_folder_path = './server/'

# Define the path to the folder containing the image to find (photo_to_find)
photo_to_find_folder_path = './photo_to_find/'

# Define the path to the destination folder where matching images will be moved
destination_folder_path = './destination/'
img = 'sanzim.jpg'
# Load the reference image (the image to find)
reference_img = face_recognition.load_image_file(os.path.join(photo_to_find_folder_path, img))
reference_encoding = face_recognition.face_encodings(reference_img)[0]

# Loop through all the images in the server folder
for filename in os.listdir(server_folder_path):
    if filename.endswith('.jpg') or filename.endswith('.png'):  # Check if the file is an image
        # Load the server image
        server_img = face_recognition.load_image_file(os.path.join(server_folder_path, filename))
        server_encoding = face_recognition.face_encodings(server_img)
        
        # If there is at least one face detected in the server image, compare the face encoding to the reference encoding
        if len(server_encoding) > 0:
            face_distance = face_recognition.face_distance([reference_encoding], server_encoding[0])
            
            # If the face distance is below a certain threshold (i.e., the images are similar enough),
            # copy the matching image to the destination folder
            if face_distance[0] < 0.6:  # Adjust the threshold value as needed
                print('Matching image found:', filename)
                shutil.copy(os.path.join(server_folder_path, filename), destination_folder_path)
    
    # Delete the image to find (photo_to_find) after all matching images have been found
    os.remove(os.path.join(photo_to_find_folder_path, img))
