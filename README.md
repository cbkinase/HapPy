# Background

## What is Haplotype Assembly?

<div align='center'>
<img src="https://i.gyazo.com/1aa1600c775fe41ce48283e7364cfe2a.png">
</div>

In humans, and many other diploid organisms, genes are present in pairs. You get one copy of a gene from your mother, and another copy from your father. Recall that during meiosis, corresponding (homologous) chromosomes pair up and exchange genetic material with each-other. However, because of the nature of this exchange process, genes located close to each-other are less likely to split up. This can result in segments of genetic material that come exclusively from one parent. 

This is what is known as a haplotype -- a set of DNA variations (often called polymorphisms) that are inherited together as a unit. This subject is of interest in a number of fields, such as disease research, precision medicine, population genetics, functional genomics, and forensics.

Although the sequence of alleles at single nucleotide polymorphism (SNP) sites can be measured through direct experimentation, the high cost of these methods has made reconstruction by computational approaches the more attractive option.

At present, there are two principal sequencing methods in the genomics space: second-generation sequencing and third-generation sequencing. Illumina, the dominant player in the second-generation sequencing space, provides short read sequencing of only up to a few hundred base pairs, but with excellent error rates on reads (estimated to be lower than 0.1%). 

In the third-generation sequencing space, we have PacBio and Oxford Nanopore, who can provide exceptionally long reads -- up to a million base pairs at a time, but with much lower per-base accuracy, with some estimates suggesting error rates may exceed 10% (~1% for PacBio HiFi). Thus, while third-generation sequencing can ameliorate certain issues related to haplotype assembly, such as dealing with highly repetitive regions or detecting long structural variants, it is far from a magic bullet.

Neither the second nor the third generation sequencing technologies directly keep track of the haplotypic origin of reads: a haplotype assembly algorithm is required for this. Due to the substantive differences between second- and third-generation sequencing technology, it is likely that novel approaches are needed for long-read data.

Of course, in the absence of sequencing errors, haplotype assembly is easy. In this situation, two fragments would conflict if and only if they come from different parents, so we could solve the problem by bipartitioning. But the reality is not so simple.

<div align='center'>
<img src="https://i.gyazo.com/b517c9c4f02aeb6078923dc8df16a589.png">
</div>

## tl;dr

Genome sequencing workflows produce contiguous DNA segments of unknown chromosomal origin. <i>De-novo</i> assemblies produce consensus sequences, but the relative haploid phase between variants is undetermined. The <i>haploid assembly problem</i> tries to compute the haplotype sequences for each chromosome: the haplotype phase of variants is inferred from assembling overlapping sequence reads.

## Haplotype Assembly Methods

#### Minimum Fragment Removal (MFR)
Treat haplotype assembly as an optimization problem where the goal is to remove the minimum number of fragments so that the remaining fragments can be partitioned into two conflict-free subsets, each representing a haplotype.

#### Maximum Parsimony Haplotyping (MPH)
Similar to MFR, but attempts to explain the observed fragments with the least number of haplotypes rather than trying to remove fragments.

#### Minimum Error Correction (MEC)
The most commonly used. In MEC, the goal is to find the two haplotypes that require the smallest number of corrections to the given fragments to eliminate all inconsistencies. MEC is an NP-hard problem, however, and generally requires heuristic solutions.
