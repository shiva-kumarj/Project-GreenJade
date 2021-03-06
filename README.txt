C:.
│   Project GreenJade.pdf
│   README.txt
│   
├───dataset
│       data.csv
│       discover.csv
│       test.csv
│       
├───notebooks
│       1-Create Dataset.ipynb
│       2-EDA.ipynb
│       3-Model Building.ipynb
│       4-Final Model.ipynb
│       5-Prediction on Test Data.ipynb
│       
└───scripts
        get_playlist.py
        model.py
        predict.py

"Project GreenJade.pdf" is the project report. Here I described my approach to the project, the findings of the Exploratory Data Analysis process, model building process, and the performance of the model on test data.

notebooks - The notebooks are numbered in sequence of project execution.
	1-Create Dataset			- Access my spotify playlists using Spotipy lib and create datasets out of it.
	2-EDA 						- Exploring and Visualizing the various facets of the songs I like and dislike.
	3-Model Building 			- Exploring the various model building algorithms, model evaluation and hyperparameter tuning.
	4-Final Model				- Build the best model with the best hyperparams from the previous notebook
	5-Prediction on Test Data 	- Model performance of the final model on the newly created test dataset.

scripts - I converted the notebooks notebooks into python scripts, so you could just run them from the commandline and you could also deploy these scripts in a docker.
	get_playlist.py - "Create Dataset.ipynb" converted to python script.
	model.py 		- "Final Model.ipynb" converted to python script.
	predict.py 		- "Prediction on Test Data.ipynb" converted to python script.
	



