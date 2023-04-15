#include <windows.h>
#include <wincrypt.h>
#include <stdio.h>

int main()
{
    const char *passw = "https://www.youtube.com/watch?v=dQw4w9WgXcQ";
    const char *passw1 = "Microsoft Enhanced RSA and AES Cryptographic Provider";
    const __int8 key[10] = {1,2,3,4,5,6,7,8,9};
    const char *toencrypt = "aaaaaaaaaaaaaaaaaaaaaaaa";
    HCRYPTPROV hProv;
    HCRYPTHASH hHash;
    HCRYPTKEY hKey;
    DWORD todwSize = (DWORD)strlen(toencrypt);
    DWORD pBuffer;
    DWORD size_Buffer = sizeof(pBuffer);
    DWORD  xBuffer;
    CryptAcquireContextW(&hProv, NULL, NULL, PROV_RSA_AES, NULL);
    CryptCreateHash(hProv, CALG_SHA_256, 0, 0, &hHash);
    CryptHashData(hHash, (BYTE *)passw, strlen(passw), 0);
    CryptGetHashParam(hHash, HP_HASHVAL, (BYTE *)pBuffer, &size_Buffer, 0);
    CryptDestroyHash(hHash);
    CryptReleaseContext(hProv, 0);
    // CryptAcquireContext(&hProv, NULL, MS_DEF_PROV, PROV_RSA_FULL, CRYPT_NEWKEYSET);

    CryptAcquireContextA(&hProv, NULL, NULL, PROV_DH_SCHANNEL, NULL);
    CryptImportKey(hProv, (BYTE *)toencrypt , sizeof(toencrypt), 0x2C, 0, NULL);
    CryptSetKeyParam(hKey,KP_MODE, (BYTE *)passw, 0);
    CryptSetKeyParam(hKey,KP_IV, (BYTE *)key, 0);
    CryptEncrypt(hKey, 0, TRUE, 0, NULL, &todwSize, todwSize);
    CryptDestroyKey(hKey);

}