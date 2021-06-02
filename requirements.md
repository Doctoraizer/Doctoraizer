
# Software Requirements
## Vision

#### What is the vision of this product?
a software program which analyzes the x-ray chest images and detect abnormality in the lung in order to help discover a possible infection with COVID-19 virus. 

#### What pain point does this project solve?
Early detection is a critical factor to control the COVID-19 spreading, we can use chest scan X-ray images to identify morphological patterns of lung lesions linked to the COVID-19

#### Why should we care about your product?
The world is still in fight with the virus and there is a real need for early discovery of the virus. Doctorizer usees advanced Machine learning algorithms to help doctors and laboratory technicians in analyzing the x-ray images in a simple click.

## Scope (In/Out)

### IN - What will your product do

The program will let the user to upload a single/set of x-ray images.
The program will analyze the uploaded images and classify them into normal or abnormal state.
The program will let the user insert patient data in order to generate an automated report with the result of thier test result.
The program will let the user access any of the previously analyzed images and give feedback in order to tune the classification algorthm.

### OUT - What will your product not do.
will not detect all of the lung related diseases and it will be restriced to pneumonia and the other types of diseases that the the model is trained to analyze. 

## Minimum Viable Product vs

#### What will your MVP functionality be?
It can determine the infection with an accuracy of 80%.

#### What are your stretch goals?
-  Store the images and results in a database
- Make more analytics of the images to know the percentage of pneumonia in the patient lungs.
- extend the ability to detect other types of diseases.
 
#### What stretch goals are you going to aim for?
-  Store the images and results in a database
- Make more analytics of the images to know the percentage of pneumonia in the patient lungs.


## Functional Requirements

List the functionality of your product. This will consist of tasks such as the following:

A user can upload a single/set of x-ray images.
A user can clear the uploaded images in the workspace.
A user can click on classify to analyze the uploaded images.
A user can insert the related patient information to the program to generate a report.
A user can generate automated reports for the uploaded data.


## Data Flow
The user needed to discover the infection of pneumonia for a patient. The user opens the program from the laboratory computer and clicks on upload button to upload the x-ray image, then the user clicks on classify to start the classification proccess, after a short time, the result appears at the screen. The user clicks on automated report, a new window appears to enter the patient data, then clicks on generate automated report, the user opens the report and print it, then closes the program.


## Non-Functional Requirements (301 & 401 only)

Non-functional requirements are requirements that are not directly related to the functionality of the application but still important to the app.


Security 
- the data is very confedential and inludes sensetive personal information, thus, a high level of securty must be ensured.
Usability 
- the program should be simple and straight-forward, the user wants to get the classification result at minimum time because time is very limited in the medical laboratory.
- other users wants to be able to use th program without previous experience. 

