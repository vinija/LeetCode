<p>Given a string <code>s</code>, return whether <code>s</code> is a <strong>valid number</strong>.<br />
<br />
For example, all the following are valid numbers: <code>&quot;2&quot;, &quot;0089&quot;, &quot;-0.1&quot;, &quot;+3.14&quot;, &quot;4.&quot;, &quot;-.9&quot;, &quot;2e10&quot;, &quot;-90E3&quot;, &quot;3e+7&quot;, &quot;+6e-1&quot;, &quot;53.5e93&quot;, &quot;-123.456e789&quot;</code>, while the following are not valid numbers: <code>&quot;abc&quot;, &quot;1a&quot;, &quot;1e&quot;, &quot;e3&quot;, &quot;99e2.5&quot;, &quot;--6&quot;, &quot;-+3&quot;, &quot;95a54e53&quot;</code>.</p>

<p>Formally, a&nbsp;<strong>valid number</strong> is defined using one of the following definitions:</p>

<ol>
	<li>An <strong>integer number</strong> followed by an <strong>optional exponent</strong>.</li>
	<li>A <strong>decimal number</strong> followed by an <strong>optional exponent</strong>.</li>
</ol>

<p>An <strong>integer number</strong> is defined with an <strong>optional sign</strong> <code>&#39;-&#39;</code> or <code>&#39;+&#39;</code> followed by <strong>digits</strong>.</p>

<p>A <strong>decimal number</strong> is defined with an <strong>optional sign</strong> <code>&#39;-&#39;</code> or <code>&#39;+&#39;</code> followed by one of the following definitions:</p>

<ol>
	<li><strong>Digits</strong> followed by a <strong>dot</strong> <code>&#39;.&#39;</code>.</li>
	<li><strong>Digits</strong> followed by a <strong>dot</strong> <code>&#39;.&#39;</code> followed by <strong>digits</strong>.</li>
	<li>A <strong>dot</strong> <code>&#39;.&#39;</code> followed by <strong>digits</strong>.</li>
</ol>

<p>An <strong>exponent</strong> is defined with an <strong>exponent notation</strong> <code>&#39;e&#39;</code> or <code>&#39;E&#39;</code> followed by an <strong>integer number</strong>.</p>

<p>The <strong>digits</strong> are defined as one or more digits.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;0&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;e&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;.&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 20</code></li>
	<li><code>s</code> consists of only English letters (both uppercase and lowercase), digits (<code>0-9</code>), plus <code>&#39;+&#39;</code>, minus <code>&#39;-&#39;</code>, or dot <code>&#39;.&#39;</code>.</li>
</ul>
