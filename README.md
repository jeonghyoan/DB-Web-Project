# Real-Time Unified Search Service for Second-Hand Trading Platforms

**Project Duration**: Apr 2022 - May 2022  

---

## Overview
This project was created to address the lack of a unified platform for real-time comparison of second-hand product prices across multiple websites, empowering users to make informed purchasing decisions effortlessly.

---

## Project Workflow

### 1. Web Crawling
- **APIs**: Collect data from Danggeun Market and Bungaejangter.  
- **Selenium**: Scrape real-time data from Jungonara.  

### 2. Data Storage
- Save the collected data in a **MySQL** database table.

### 3. Data Integration
- Combine data from different sources (Danggeun Market, Bungaejangter, Jungonara) into a unified MySQL table.
- Perform filtering to remove irrelevant or incomplete records (e.g., missing prices or images).  

### 4. Data Preprocessing
- Remove Irrelevant Keywords: Delete rows containing unwanted keywords in product titles (e.g., "삽니다", "구해요", "교환", "나눔", "기부").
- Remove Incomplete Data: Delete rows where critical fields (e.g., price, image) are NULL.
- Format and Standardize Timestamps: Convert published_at values (e.g., "몇초 전", "몇분 전") into a standard datetime format.
- Remove Outliers: Exclude extreme values based on price.(e.g., 99999원)

### 5. Web Service Implementation
- Develop a web-based service using **PHP**.
- Use **HTML, CSS**, and **PHP** to implement the frontend.  

---

## Challenges Faced
- **Data Crawling & Integration**: Aggregating data from multiple platforms required overcoming various API limitations and data formatting issues.
- **Real-Time Processing**: Ensuring that the data was updated promptly presented significant technical challenges, particularly regarding system performance and latency.<br><br>

---

## Results

1. Home Screen  
   <img width="600" alt="1" src="https://github.com/user-attachments/assets/f1025685-2347-4d3a-8ccd-5393554fcffd" /><br><br>

2. Search for Items to Purchase  
   <img width="600" alt="2" src="https://github.com/user-attachments/assets/b69d3424-7721-461c-a277-8c083f44d05f" /><br><br>

3. Search Results Screen (Average Price)  
   <img width="600" alt="3" src="https://github.com/user-attachments/assets/50e9b08f-5383-4e56-96db-cb54367482f9" /><br><br>
   <img width="600" alt="4" src="https://github.com/user-attachments/assets/2db6bf38-02a0-4c3e-b9e8-238090739a11" /><br><br>

4. Click on Item to Go to the Second-Hand Platform  
   <img width="600" alt="5" src="https://github.com/user-attachments/assets/d0fad1e4-190b-4a56-a1c9-7421bf156e5d" /><br><br>


