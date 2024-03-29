<h1 align='center'> Document Classification System using Multinomial Naive Bayes Theorem </h1>
<br>

This note is to log the development process of the overall system. So let's begin 
<br>
<h2> What is this system about ? </h2>
<div align='left'>
    <p>&nbsp;&nbsp; The idea is we are going to build a system which can read any pdf and build a profile using vectorizer like count vectorizer this will make our system capable of understanding what kind of words are there in such document type and hence will be able to predict any new document as one of the previous datatypes </p>
</div>
<br>

<h2> How does it work </h2>

<div align='left'>
    <p>&nbsp;&nbsp; Initially we train our model to understand datas from past which are labeled as particular topic realted or not. Then we are going to use various unknown data for inference testing and see how well it performs. </p>
</div>
<br>

<h2> Where can  it work </h2>

<div align='left'>
    <p>&nbsp;&nbsp; Our system as of now works only with pdf documents but we can make it adaptable to work with any datatype provided we can read the text from that particular file.</p>
</div>
<br>

<h3>Let's learn more </h3>
<br>
<div align='left'>
    <h3><b> Multinomial Naive Bayes </b></h3>
    <img src='https://universe-files.vzaar.com/vzaar/vz2/daf/target/vz2dafd66cf49442ad9c840b1e6d74b211.jpg'>
    <p> We are going to take a bunch of words convert it into dataset having words and title such that the first column of dataste consists all the words required for the particular task of classification and title consists all the label assigned to a particular class. </p>
    <br>
    <ul> Libraries used </ul>
        <li> Pymupdf (fitz) </li>
        <li> Pandas </li>
        <li> Scikit-learn </li>
    </ul>
<br>
<br>
<div align='right'>
    <p> First we are going to use <b>  Preprocess </b> to create folders where all files are stored then we are going to use <b> Dataset Generator</b> to  generate an excell file with all the details that we are going to use for training purpose. Finally we are going to use <b> classifier.py </b> for classification purpose  of the files
</div>
<br>
<br>


<div align='left'>
    <p> This bag of words approach can be swtiched with tfidf approach to test for new possible words and working on how it can be used to make a better classifcation model for special terms and words </p>
</div>
<br>
<br>


<div align='right'>
    <p> This project can be scaled up to include deep learning approach to have feature extraction in and of itself. </p>
</div>

<br>

<div align='center'>
    <p> Documentation on Progress !! </p>
</div>
