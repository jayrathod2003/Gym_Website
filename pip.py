import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
import numpy as np
import pandas as pd
import tensorflow as tf
from pathlib import Path

class ObjectDetectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Object Detection App")
       
        self.train_path = Path("C:/Users/shind/OneDrive/Desktop/ann/data/training_images")
        self.test_path = Path("C:/Users/shind/OneDrive/Desktop/ann/data/testing_images")
       
        # Create the widgets
        self.label = tk.Label(root, text="Object Detection App")
        self.label.pack()
       
        self.load_data_button = tk.Button(root, text="Load Data", command=self.load_data)
        self.load_data_button.pack()
       
        self.train_button = tk.Button(root, text="Train Model", command=self.train_model)
        self.train_button.pack()
       
        self.test_button = tk.Button(root, text="Test Model", command=self.test_model)
        self.test_button.pack()
       
        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.pack()
       
        self.model = None
        self.train_data = None
       
    def load_data(self):
        # Load your data here
        try:
            train = pd.read_csv("C:/Users/shind/OneDrive/Desktop/ann/data/train_solution_bounding_boxes (1).csv")
            train[['xmin', 'ymin', 'xmax', 'ymax']] = train[['xmin', 'ymin', 'xmax', 'ymax']].astype(int)
            train.drop_duplicates(subset='image', inplace=True, ignore_index=True)
            self.train_data = train
            messagebox.showinfo("Success", "Data loaded successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error loading data: {e}")
   
    def train_model(self):
        # Train your model here
        try:
            # Your training code here
            messagebox.showinfo("Success", "Model trained successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error training model: {e}")
           
    def test_model(self):
        # Test your model here
        try:
            # Your testing code here
            messagebox.showinfo("Success", "Model tested successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error testing model: {e}")

root = tk.Tk()
app = ObjectDetectionApp(root)
root.mainloop()