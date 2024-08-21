<p><strong>Balanced</strong> strings are those that have an equal quantity of <code>&#39;L&#39;</code> and <code>&#39;R&#39;</code> characters.</p>

<p>Given a <strong>balanced</strong> string <code>s</code>, split it into some number of substrings such that:</p>

<ul>
	<li>Each substring is balanced.</li>
</ul>

<p>Return <em>the <strong>maximum</strong> number of balanced strings you can obtain.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;RLRRLLRLRL&quot;
<strong>Output:</strong> 4
<strong>Explanation:</strong> s can be split into &quot;RL&quot;, &quot;RRLL&quot;, &quot;RL&quot;, &quot;RL&quot;, each substring contains same number of &#39;L&#39; and &#39;R&#39;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;RLRRRLLRLL&quot;
<strong>Output:</strong> 2
<strong>Explanation:</strong> s can be split into &quot;RL&quot;, &quot;RRRLLRLL&quot;, each substring contains same number of &#39;L&#39; and &#39;R&#39;.
Note that s cannot be split into &quot;RL&quot;, &quot;RR&quot;, &quot;RL&quot;, &quot;LR&quot;, &quot;LL&quot;, because the 2<sup>nd</sup> and 5<sup>th</sup> substrings are not balanced.</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;LLLLRRRR&quot;
<strong>Output:</strong> 1
<strong>Explanation:</strong> s can be split into &quot;LLLLRRRR&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s[i]</code> is either <code>&#39;L&#39;</code> or <code>&#39;R&#39;</code>.</li>
	<li><code>s</code> is a <strong>balanced</strong> string.</li>
</ul>
