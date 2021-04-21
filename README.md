***Задание 5.*** Реализовать программно пример построения LR(0)-
анализатора для разбора цепочки (n+n)+n в грамматике:

E→E+T
E→T
T→n
T→(E)


***Заполнение управляющей таблицы***
Пронумеруем правила для выполнения свертки:

(0) E0→E
(1) E→E+T
(2) E→T
(3) T→n
(4) T→(E)

Управляющая таблица будет выглядеть так:

<table>
	<tr>
		<th></th><th>E</th><th>T</th><th>n</th><th>+</th><th>(</th><th>)</th><th>$</th>
	</tr>
	<tr>
		<td>0</td><td>1</td><td>2</td><td>s(3)</td><td></td><td>s(4)</td><td></td><td></td>		
	</tr>
	<tr>
		<td>1</td><td></td><td></td><td></td><td>s(5)</td><td></td><td></td><td>r(0)</td>
	</tr>
	<tr>
		<td>2</td><td></td><td></td><td></td><td>r(2)</td><td></td><td>r(2)</td><td>r(2)</td>
	</tr>
	<tr>
		<td>3</td><td></td><td></td><td></td><td>r(3)</td><td></td><td>r(3)</td><td>r(3)</td>
	</tr>
	<tr>
		<td>4</td><td>6</td><td>2</td><td>s(3)</td><td></td><td>s(4)</td><td></td><td></td>
	</tr>
	<tr>		
		<td>5</td><td></td><td>7</td><td>s(3)</td><td></td><td>s(4)</td><td></td><td></td>		
	</tr>
	<tr>
		<td>6</td><td></td><td></td><td></td><td>s(5)</td><td></td><td>s(8)</td><td></td>	
	</tr>
	<tr>
		<td>7</td><td></td><td></td><td></td><td>r(1)</td><td></td><td>r(1)</td><td>r(1)</td>
	</tr>
	<tr>
		<td>8</td><td></td><td></td><td></td><td>r(4)</td><td></td><td>r(4)</td><td>r(4)</td>
	</tr>
</table>
