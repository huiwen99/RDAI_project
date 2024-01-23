# RDAI Project - AI in Production
This project does an image classification using a pre-trained ResNet101 on the Imagenet dataset.

## Instructions to run
1. Run the following commands in the terminal:  
```
cd build
docker compose up
```
2. In your browser, go to http://0.0.0.0:5002.
3. On the left column, upload any image that has a corresponding class in the Imagenet dataset.  
A few test images are available in the `test_images` folder.  
4. Click on the `Submit` button.  
The model's prediction of the class of the image will be displayed on the right column's text box.
5. Repeat steps 3-4 as many times as you want. After you are done, press `Ctrl+C` in your terminal.  
Then, run the following in the terminal:  
```
docker compose down
```


