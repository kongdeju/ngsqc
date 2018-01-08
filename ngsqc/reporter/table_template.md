{% macro add_table(table) -%}

{% for i in range(table.nrows) -%}
{% if i == 0 -%}
{% for cell in table.row_values(i) -%}
        |{{ cell }}
{%- endfor %}|
{% for j in range(table.ncols) -%}
            |-
{%- endfor %}|
{%- else %}
{% for cell in table.row_values(i) -%}
     |{{ cell }}
{%- endfor %}|
{%- endif %}
{%- endfor %}

{% endmacro -%}

{% macro getName(path) -%}
{% set item = path.split("/")[-3].rsplit("_",1)[0] -%}
{{ item }}
{%- endmacro %}

## 中科院计算所 • 北京中科晶云科技有限公司

## 原始数据质量评估报告

## 1.质控介绍
数据质控，旨在查看原始数据质量信息，包括原始数据q20,q30,gc含量等。


## 2.数据分析流程

利用`fastqc`对每个fastq文件进行质量统计，并汇总每个fastq的信息


##3 具体分析及结果统计

###3.1 测序质量评估

####3.1.1 原始序列数据

高通量测序(如Illumina HiSeqTM4000/MiseqTM/X-Ten)得到的原始图像数据文件经碱基识别(Base Calling)分析转化为原始测序序列(Sequenced Reads)，我们称之为 Raw Data或Raw Reads，结果以 FASTQ (简称为fq)文件格式存储，其中包含测序序列(reads)的序列信息以及其对应的测序质量信息。

FASTQ格式文件中每个read由四行描述，如下：

|   |
| ----------------------------------------------------------------------------------------------------------------------- |
| @ST-E00600:21:H2HYGALXX:1:1101:1307:1000 1:N:0:ACCTCCAA  |
|  GGAAATGCCCTGTCCACACAGGATAGAAAAGTGTGACCTCCGGGTTCAAGAATTTTGTAGTCCGTGATCCTGGGTGCACTGGCCCCATAGTTATTCTTACCCATGCTTCCTTCCTGTCATCGTTGACAAGCCCCAAGATATATTTCTAGT |
| +  |
|  AAJFFFFJJJJJJAJFJJAJJJJFFAJFJJ<JJJFJFFJAAJJJJJAJJAJJJAFJJFJJJFAJJAJAFJAFJJJJAJJJAJFJAFJ>JFJJJJAJJJJFJJJJJJAFJJJJJJJJJFJAAJJFJJFJ>FFAFFFJJJ-J-JJFJJJJJ- |


其中：

第一行以“@”开头，随后为Illumina 测序标识别符和描述文字；

第二行是碱基序列；

第三行以“+”开头，随后为Illumina 测序标识别符(选择性部分)；

第四行是对应碱基的测序质量，该行中每个字符对应的 ASCII 值减去 33，即为碱基质量值。

Illumina测序标识符详细信息如表3.2所示：


|   |   |
| ------------ | ------------------------------------------------------------------------------------------- |
| @ST-E00600  | Instrument - unique identifier of the sequencer  |
| 21  |  run number - Run number on instrument |
| H2HYGALXX  |  FlowCell ID - ID of flowcell |
| 1  |  LaneNumber - positive integer |
|  1101 | TileNumber - positive integer  |
| 1307  |  X - x coordinate of the spot. Integer which can be negative |
| 1000  |  Y - y coordinate of the spot. Integer which can be negative |
|  1 |  ReadNumber - 1 for single reads; 1 or 2 for paired ends |
| N  |  whether it is filtered - NB: Y if the read is filtered out, not in the delivered fastq file, N otherwise |
| 0  | control number - 0 when none of the control bits are on, otherwise it is an even number  |
|  ACCTCCAA |  Illumina index sequences |


####3.1.2 不同位置的碱基质量

在测序过程中会存在一定的错误率，测序错误率分布检查可以反映测序数据的质量。如果测序错误率用e表示，Illumina HiSeqTM4000/MiseqTM的碱基质量值用Qphred表示，则有：Qphred=-10log10(e)。

Illumina 1.9版本中碱基识别与Phred分值之间的简明对应关系见下表3.3所示：

<center>表3.3 Illumina测序标识符详细信息</center>

| Phred分值  |  不正确的碱基识别 |  碱基正确识别率 |  Q-sorce |
| ------------ | ------------ | ------------ | ------------ |
| 10  | 1/10     | 90%     | Q10  |
| 20  | 1/100    | 99%     | Q20  |
| 30  | 1/1000   | 99.9%   | Q30  |
| 40  | 1/10000  | 99.99%  | Q40  |

测序错误率分布具有以下两个特点：

a) 测序错误率会随着测序序列(Reads)长度的增加而升高，这是由测序过程中化学试剂的消耗导致的，并且此现象为illumina高通量测序平台的共有特征

b) 前10个碱基的位置也会发生较高的测序错误率，而这个长度也正好等于在建库过程中所需要的随机引物的长度。所以推测这部分碱基的测序错误率较高的原因是：随机引物与模版的不完全结合。一般情况下，单个碱基位置的测序错误率应该低于1%。

对本项目所有测序数据进行不同位置的碱基错误率进行评估，结果如图3.1所示，横轴为测序reads长度，虚线左边为R1端fastq错误率统计，虚线右边为R2端fastq错误率统计（如果为SE测序，则只有R1端错误率统计），纵轴为该位点的平均错误率。


使用FastQC工具对本课题中测序数据进行不同位置的碱基质量评估，结果如图3.2所示，横轴为测序reads长度，纵轴为质量得分

{% if per_base_quality %}
	![]({{ per_base_quality }})
{% endif %}


<center>图3.2 测序样本{{ getName(per_base_quality) }}的碱基质量分布</center>

