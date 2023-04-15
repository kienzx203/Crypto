# **AES**

## **Cấu trúc AES**

- Ở cấp độ cao, AES-128 bắt đầu với "lịch trình chính" và sau đó chạy 10 vòng trên một trạng thái. Trạng thái bắt đầu chỉ là khối văn bản gốc mà chúng tôi muốn mã hóa, được biểu diễn dưới dạng ma trận byte 4x4. Trong suốt 10 vòng, trạng thái liên tục được sửa đổi bởi một số phép biến đổi nghịch đảo.

- Dưới đây là tổng quan về các giai đoạn mã hóa AES:

![](./img_AES/1.png)

`1. KeyExpansion or Key Schedule`

 From the 128 bit key, 11 separate 128 bit "round keys" are derived: one to be used in each AddRoundKey step.

`2. Initial key addition`

 AddRoundKey - the bytes of the first round key are XOR'd with the bytes of the state.

`3. Round - this phase is looped 10 times, for 9 main rounds plus one "final round"`

  a) SubBytes - each byte of the state is substituted for a different byte according to a lookup table ("S-box").

 b) ShiftRows - the last three rows of the state matrix are transposed—shifted over a column or two or three.

 c) MixColumns - matrix multiplication is performed on the columns of the state, combining the four bytes in each column. This is skipped in the final round.

 d) AddRoundKey - the bytes of the current round key are XOR'd with the bytes of the state.

![](./img_AES/2.png)
