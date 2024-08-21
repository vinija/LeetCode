<p>Given a string <code>s</code> and a character <code>letter</code>, return<em> the <strong>percentage</strong> of characters in </em><code>s</code><em> that equal </em><code>letter</code><em> <strong>rounded down</strong> to the nearest whole percent.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;foobar&quot;, letter = &quot;o&quot;
<strong>Output:</strong> 33
<strong>Explanation:</strong>
The percentage of characters in s that equal the letter &#39;o&#39; is 2 / 6 * 100% = 33% when rounded down, so we return 33.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;jjjj&quot;, letter = &quot;k&quot;
<strong>Output:</strong> 0
<strong>Explanation:</strong>
The percentage of characters in s that equal the letter &#39;k&#39; is 0%, so we return 0.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
	<li><code>letter</code> is a lowercase English letter.</li>
</ul>
