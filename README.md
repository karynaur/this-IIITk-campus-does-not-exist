# this-IIITk-campus-does-not-exist

## Inspiration

We decided to make a model that generates images of IIITk after successfully completing our first semester online 

## What it does

Trained on over 2000 images of IIITk campus, the StyleGAN2 model can successfully generate beautiful images of the campus 
## How we built it
We started of by trimming the [video](https://youtu.be/kG9WpDUQZ7Y) to extract the parts that had the campus. Using OpenCV we extracted and saved the frames. After scraping some more images from google photos we had over 2000 images of the elegant campus.
We then took a model trained on images of church buildings and trained it with the campus photos for ~24 hours to get a model that could successfully generate **fake** images. 

## Colab Notebook
[Colab](https://colab.research.google.com/drive/1reT4mpoqwjiphpTgQB5QvDQ1FJHEXEQp?usp=sharing)

## Acknolwdgements
1. [StyleGan2(https://github.com/NVlabs/stylegan2)

