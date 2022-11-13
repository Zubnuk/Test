*Дана матрица, нужно найти определитель n=12 порядка*

$$      
A =       
 \begin{pmatrix}      
  11 & 2 & 0 & \cdots & 0 & 0 \\      
  14 & 11 & 2 & \cdots & 0 & 0 \\      
  0 & 14 & 11 & \cdots & 0 & 0 \\      
  \vdots  & \vdots & \vdots & \ddots & \vdots & \vdots  \\      
  0 & 0 & 0 & \cdots & 11 & 2 \\      
  0 & 0 & 0 & \cdots & 14 & 11       
 \end{pmatrix}      
$$ 


$1) \bigtriangleup_n = 11 * \bigtriangleup_{n-1} - 2*14 * \bigtriangleup_{n-2}$

$\lambda^n = 11 * \lambda^{n-1} - 28 * \lambda^{n-2}$

$2) \lambda^n - 11 * \lambda^{n-1} + 28 * \lambda^{n-2} = 0| :\lambda^{n-2}$

$λ ^2 - 11λ + 28 = 0$

$D = 121 - 28*4 = 9$

$\lambda_1 = 7, \lambda_2 = 4$

$3)\bigtriangleup_n  = C_1 * \lambda_1^n + C_2 * \lambda_2^n$

$\text{Система:}$

$\left\{\begin{matrix}
11 = 7 * C_1 +4 * C_2\\ 
93 = 49 * C_1 + 16 * C_2
\end{matrix}\right.$

$\text C_1 = \frac73, C_2 = - \frac43$

$\text{Тогда: }$

$\bigtriangleup_n  = \frac73 * 7^n - \frac43 * 4^n$

$\bigtriangleup_n  = \frac13 *  (7^{n+1} - 4^{n+1})$

$\bigtriangleup_{12}  = \frac13 *  (7^{13} - 4^{13})=32273967181$

$\text{Ответ: 32273967181}$
