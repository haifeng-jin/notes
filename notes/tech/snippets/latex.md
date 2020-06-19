# LaTex
#tech/snippet
How to add?
\bibliographystyle{abbrv}
\begin{thebibliography}{99}
\bibitem{gSK0}
A. Maccari, {\em Phys. Lett. A} {\bf 265} (2000) 187.

\bibitem{intro1}
C. F. Liu, Z.D. Dai, {\em Appl. Math. and Comput.} {\bf 206} (2008) 272.

\bibitem{intro2}
Z. H. Yang, {\em Commun. Theor. Phys.} {\bf 46} (2006) 807.
\end{thebibliography}

How to Cite?
bilinear~\cite{Hirota1,Hirota2,Hirota3}, Darboux transformation~\cite{dar1,dar2,dar3}, Bell polynomial~\cite{bell1,bell2,bell3} and B\"{a}cklund transformation (BT)~\cite{BT1}.

Note: The default order of the bibliography is the order they appear in the list.

The title of bibliography is "Bibliography" or "Reference" depend on what document class you use.

Command line is "latex filename.tex" to make a dvi file, "pdflatex filename.tex" to make a pdf file.

picture:
\includegraphics[height=8cm]{fig1.eps}

table:

\begin{center}
\begin{tabular}{@{}llr@{}}
\toprule
\multicolumn{3}{c}{Statistical Feature}\\
\midrule
No. &Name &Type\\
\midrule
1 &time stamp &Text \\
3 &IMSI &Number \\
4 &number of HTTP links with same IMSI in 2 min &Number \\
5 &number of HTTP packet sent with same IMSI in 2 min &Number \\
6 &number of HTTP packet recieved with same IMSI in 2 min &Float \\
7 &number of Bytes sent with same IMSI in 2 min &Number \\
8 &number of Bytes recieved with same IMSI in 2 min &Number \\
9 &send-to-recieve ratio of Bytes with same IMSI in 2 min &Float \\
10 &ratio of packet with the same destination IP in 5 min &Float \\
11 &ratio of packet with the same destination IP and protocal type in 5 min &Float \\
12 &number of PDP sessions originated by the user &Number \\
\bottomrule
\end{tabular}
\end{center}

break long urls:

\usepackage[hyphens]{url}

\url{http:.....}