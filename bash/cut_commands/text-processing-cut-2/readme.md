# text-processing-cut-2

# 目次

<!-- @import "[TOC]" {cmd="toc" depthFrom=2 depthTo=6 orderedList=false} -->
<!-- code_chunk_output -->

- [URL](#url)
- [感想](#感想)

<!-- /code_chunk_output -->

## URL

https://www.hackerrank.com/challenges/text-processing-cut-2/problem

## 感想

- 最初なぜ躓いたか分からなかったけどスペースが余分だったようである
    - (誤): `cat | cut -c 2, 7`
    - (正): `cat | cut -c 2,7`
