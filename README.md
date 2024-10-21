# dccc

A tool to help in recovering a forgotten passphrase (using a pre-defined wordlist a.k.a. dictionary attack) for a wallet created with [Dogecoin Core](https://github.com/dogecoin/dogecoin). 

## Requirements
1. Python 3
2. [dogecoin-cli.exe](https://github.com/dogecoin/dogecoin/releases/tag/v1.14.8) (from Dogecoin Core 1.14.8 | SHA256: 406BEEBE9AA92589EBBD4A00194FDE04C7BF1253EBE479A8379CBEF2C6EED057)
3. [dogecoind.exe](https://github.com/dogecoin/dogecoin/releases/tag/v1.14.8) (from Dogecoin Core 1.14.8 | SHA256: 6BD5E44F7671CC80E20210108E60CEF98EA7D66F5A5D278C6073AA5F1EF4619B)

Note: You'll most likely want to download the same Dogecoin Core version that was used to initially create the wallet or this might not work/haven't tried. (This tool was tested against a wallet which was created with version 1.14.8)

## Instructions (Windows 10)
1. IMPORTANT: MAKE A BACKUP OF YOUR EXISTING WALLET FIRST. The default location and file is typically `%appdata%\Dogecoin\wallet.dat`
2. Copy your target wallet to `%appdata%\Dogecoin\wallet.dat`
3. Run `dogecoind.exe`
4. Run the tool: `python dccc.py wordlist.txt dogecoin-cli.exe`

```
C:\> python dccc.py words.txt dogecoin-cli.exe
[-] Invalid passphrase: 'bad passphrase'
[-] Invalid passphrase: 'i wish i could remember my passphrase'
[-] Invalid passphrase: 'test 123 passphrase'
[-] Invalid passphrase: 'DogePassphrase132'
[-] Invalid passphrase: 'not my passphrase'
-------------------------------------------------------------
[+] Potential match: DogePassphrase133
-------------------------------------------------------------
```


THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


