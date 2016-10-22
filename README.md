ATCG for SublimeText
====================

Nucleotide syntax highlighting and reverse complement support. This is handy for "stare at the screen and squint" DNA analysis. Upgrade from hackerfriendly/ACTG.

Features
--------

* Choose 'Nucleotides' syntax highlighting to colorize ACTG and N.
* Automatically associates .fa, .fasta, .fq, .fastq, .sam, and .vcf files.
* Three kinds of conversion are supportted: 
  * Make a selection and hit Control-Shift-R (or Command-Shift-R on Mac) to do **reverse**.
  * Control-Shift-C (or Command-Shift-C on Mac) to make **complementation**.
  * command Ctrl+R, Ctrl+C (this mean hold Ctrl, press R then press C, release Ctrl) to replace it with **reverse complement**.

Bugs
----

* ACTG and N are simply highlighted in place, which can make for some interestingly colored VCF comments and quality strings. A more clever regex would help, if only I could fathom the tmLanguage backreference match syntax.

Patches welcome.

Releases
--------

* 1.0.0: Initial release, 2016-10-20
