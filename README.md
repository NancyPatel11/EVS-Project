# EVS-Project

## Installation

To get started with the project, follow these steps:

1. Clone this repository.

```json
git clone https://github.com/NancyPatel11/EVS-Project.git
```

2. Install the necessary dependencies.
   Run the following command in your terminal. Make sure you are at the correct path (home) of the cloned repository.

```json
pip install numpy pandas matplotlib seaborn tensorflow keras tqdm scikit-learn fastapi uvicorn pillow
```

## Run the project.
In the api.py file, simply press the run button to run the code. You will see a localhost being started up in your terminal as shown in the image below. Open this localhost on your browser.
![alt text](/api_working_screenshots/1.png)

You will be directed to the following page:
![alt text](/api_working_screenshots/2.png)

Next, type `/docs` at the end of the url as shown below:
![alt text](/api_working_screenshots/3.png)

You will get directed to the FASTAPI homepage. Here, you can see the `uploadfile` post request. Click on it to expand it. You will see the option `try it out`.
![alt text](/api_working_screenshots/4.png)

Now click on the `try it out` button, you will see an image upload section where you can choose any image of the garbage from your computer:
![alt text](/api_working_screenshots/5.png)

Once you upload a the image of the garbage, click on execute. Our model will then be called in the backend and you will see the classification result along with the model confidence as shown below:
![alt text](/api_working_screenshots/6.png)
