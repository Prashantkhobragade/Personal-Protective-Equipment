## **Personal Protective Equipment**

This project is an implementation of PPE (Personal Protective Equipment) object detection using YOLOv8, a state-of-the-art deep learning model for object detection. The goal of this project is to detect and classify different PPE items, such as helmets, vests, goggles, and masks, in video streams.

## **Tech Stack Used**

  * Python 3.9
  * OpenCV
  * Ultralytics (YOLOv8)
  * FastAPI
    
## **Use Case**

### Construction Site Access Control:
The model can be employed at entry and exit points of construction sites to identify and grant access only to authorized personnel wearing the proper safety gear, helping to maintain a safe working environment and prevent unauthorized access.


### Result
![Training_Result](https://github.com/Prashantkhobragade/Personal-Protective-Equipment/blob/main/Report/results.png)


## **How To Run?**

 **step 1. Clone the repository**
 
  ```bash
    https://github.com/Prashantkhobragade/Personal-Protective-Equipment.git
  ```
 **step 2. Create a conda environment after opening the repository**

  ```bash
   conda create -p PPE python=3.9 -y
  ```
  ```bash
    conda activate PPE/
  ```

 **step 3. Install the requirements**

  ```bash
   pip install -r requirements.txt
  ```
 **step 4. Run the application server**

 ```bash
  uvicorn service.app:app
 ```
 **step 5. Prediction application**

 ```bash
  http://localhost:8000/docs
 ```

## **Future Improvements**
Here are a few potential areas for future improvement and development of the PPE Detection CV Project:

 **1. Model Ensembling:** Combine multiple trained YOLOv8 models through model ensembling techniques, such as weighted average or non-maximum suppression (NMS), to improve detection accuracy and reduce false positives.

 **2. Hyperparameter Tuning:** Fine-tune the hyperparameters of the YOLOv8 model, such as learning rate, batch size, and number of epochs, to optimize the training process and improve detection accuracy.

**3. User Interface:** Develop a user-friendly web or mobile application to visualize the PPE detection results and provide an intuitive interface for users to interact with the model.

## **Acknowledgments**
 * This project is based on the YOLOv8 implementation by [Prashant Khobragade](https://github.com/Prashantkhobragade) and [Ultralytics](https://github.com/ultralytics).

## **License**
 [MIT License](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt)
 
 Feel free to contribute to this project by opening issues, submitting pull requests, or suggesting improvements. Happy detecting!

