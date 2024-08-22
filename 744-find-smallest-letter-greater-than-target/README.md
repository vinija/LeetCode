<p>You are given an array of characters <code>letters</code> that is sorted in <strong>non-decreasing order</strong>, and a character <code>target</code>. There are <strong>at least two different</strong> characters in <code>letters</code>.</p>

<p>Return <em>the smallest character in </em><code>letters</code><em> that is lexicographically greater than </em><code>target</code>. If such a character does not exist, return the first character in <code>letters</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> letters = [&quot;c&quot;,&quot;f&quot;,&quot;j&quot;], target = &quot;a&quot;
<strong>Output:</strong> &quot;c&quot;
<strong>Explanation:</strong> The smallest character that is lexicographically greater than &#39;a&#39; in letters is &#39;c&#39;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> letters = [&quot;c&quot;,&quot;f&quot;,&quot;j&quot;], target = &quot;c&quot;
<strong>Output:</strong> &quot;f&quot;
<strong>Explanation:</strong> The smallest character that is lexicographically greater than &#39;c&#39; in letters is &#39;f&#39;.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> letters = [&quot;x&quot;,&quot;x&quot;,&quot;y&quot;,&quot;y&quot;], target = &quot;z&quot;
<strong>Output:</strong> &quot;x&quot;
<strong>Explanation:</strong> There are no characters in letters that is lexicographically greater than &#39;z&#39; so we return letters[0].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= letters.length &lt;= 10<sup>4</sup></code></li>
	<li><code>letters[i]</code> is a lowercase English letter.</li>
	<li><code>letters</code> is sorted in <strong>non-decreasing</strong> order.</li>
	<li><code>letters</code> contains at least two different characters.</li>
	<li><code>target</code> is a lowercase English letter.</li>
</ul>
