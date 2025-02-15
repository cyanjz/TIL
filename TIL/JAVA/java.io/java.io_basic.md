# Basics
본 문서에서는 I/O에서 고려해야할 기본적인 사항을 다룹니다.
1. Encoding/decoding
- InputStream, Reader / OutputStream, Writer를 사용할 때는 encoding에 유의.
- Byte buffer 형성하여 IO 다룰 때에도 반드시 encoding에 유의해야함. ASCII에 해당하는 문자는 1byte로 표현 가능하기 때문에 byte buffer의 한칸을 차지하지만, 다른 문자의 경우에는 두칸 이상을 차지할 수 있다.
- 
2. 