<h2> Text Anomaly in parallel</h2>
<p>- The code finds out the most hostile tweets, most negetive, most positive tweets. </p>
<p>- Files:</p><ul>
<li><b> Tweet.py :</b>  To extract and display all Tweets from <code>*TwitterData.txt</code> file.</li>
<li><b> HostileSetCreator.py :</b>  This program is used to  extract all the Hostile words from <code> Words.txt </code></li>
<li><b> HostileSet.pyc :</b> This has a list of all the extracted Hostile words.</li>
<li><b> Anomoly.py :</b>  The main progarm to find most hostile tweets, most negetive, most positive tweets </li>
</ul>
<pre>
<p>- Flow of Anomaly.py : 
        
        1)Find the TF/IDF of each tweet.
        
        2)Using the 1.5 IQR method to remove the outliers.
        
        3)Find the hostility factor for each tweet.
        
        4)Using Sentiment Analysis find the sentiment value of each tweet.
        
        5)Display the most postive and negetive tweets based on the sentiment value.
        
        6)Display top 0.05% most hostile tweets based on the Hostility factor calculated.</p>
</pre>

<p>
- 3, 4 can be done ind parallel
- I use <code> Multiprocessing </code> Module of pyhton to spawn two threads which do 3, 4 in parallel/Concurrently.
</p>

<h2> How to run the code</h2> 
Use the command:  
<pre><code> Pyhton Anomaly.py</code></pre>
