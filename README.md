# Background

## What is Haplotype Assembly?

<div align='center'>
<img src="https://i.gyazo.com/1aa1600c775fe41ce48283e7364cfe2a.png">
</div>

<br>

In humans, and many other diploid organisms, chromosomes are present in pairs. You get one copy of a chromosome from your mother, and another copy from your father. When we sequence a diploid organism's genome, we get a mix of both copies of each chromosome. 

However, most sequencing technologies cannot distinguish which sequence comes from the maternal chromosome and which comes from the paternal chromosome. This can be problematic when studying the effects of certain genes or mutations, as their impact can often depend on the specific combination of alleles on both chromosomes (i.e., the haplotype). Haplotype assembly is also of interest in a number of other fields, such as precision medicine, population genetics, and forensics.

Although the sequence of alleles at single nucleotide polymorphism (SNP) sites can be measured through direct experimentation, the high cost of these methods has made reconstruction by computational approaches the more attractive option. This is done by grouping together fragments that likely come from the same parent. This task is complicated by the fact that errors can occur during the sequencing process, leading to mismatches between the fragments and the true haplotypes.

At present, there are two principal sequencing methods in the genomics space: second-generation sequencing and third-generation sequencing. Illumina, the dominant player in the second-generation sequencing space, provides short read sequencing of only up to a few hundred base pairs, but with excellent error rates on reads (estimated to be lower than 0.1%). 

In the third-generation sequencing space, we have PacBio and Oxford Nanopore, who can provide exceptionally long reads -- up to a million base pairs at a time, but with much lower per-base accuracy, with some estimates suggesting error rates may exceed 10% (~1% for PacBio HiFi). Thus, while third-generation sequencing can ameliorate certain issues related to haplotype assembly, such as dealing with highly repetitive regions or detecting long structural variants, it is far from a magic bullet.

Neither the second nor the third generation sequencing technologies directly keep track of the haplotypic origin of reads: a haplotype assembly algorithm is required for this. Due to the substantive differences between second- and third-generation sequencing technology, it is likely that novel approaches are needed for long-read data.

Of course, in the absence of sequencing errors, haplotype assembly is easy. In this situation, two fragments would conflict if and only if they come from different parents, so we could solve the problem by bipartitioning. But the reality is not so simple.

<br>

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
