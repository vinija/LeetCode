<p>There is a strange printer with the following two special properties:</p>

<ul>
	<li>The printer can only print a sequence of <strong>the same character</strong> each time.</li>
	<li>At each turn, the printer can print new characters starting from and ending at any place and will cover the original existing characters.</li>
</ul>

<p>Given a string <code>s</code>, return <em>the minimum number of turns the printer needed to print it</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aaabbb&quot;
<strong>Output:</strong> 2
<strong>Explanation:</strong> Print &quot;aaa&quot; first and then print &quot;bbb&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aba&quot;
<strong>Output:</strong> 2
<strong>Explanation:</strong> Print &quot;aaa&quot; first and then print &quot;b&quot; from the second place of the string, which will cover the existing character &#39;a&#39;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
</ul>
