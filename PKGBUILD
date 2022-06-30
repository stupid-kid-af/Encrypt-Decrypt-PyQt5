# This is an example PKGBUILD file. Use this as a start to creating your own,
# and remove these comments. For more information, see 'man PKGBUILD'.
# NOTE: Please fill out the license field for your package! If it is unknown,
# then please put 'unknown'.

# Maintainer: Your Name <youremail@domain.com>
pkgname=Encrypt-Decrypt-PyQt5
pkgver=1.0
pkgrel=1
arch=(x86_64)
url="https://github.com/stupid-kid-af/Encrypt-Decrypt-PyQt5"
license=('MIT')
provides=(encd)
install=
source=("git+$url")
noextract=()
md5sums=('SKIP')
validpgpkeys=()

build() {
	cd Encrypt-Decrypt-PyQt5
	pyinstaller --onefile --windowed application.py
}
package() {
	cd Encrypt-Decrypt-PyQt5
        cd dist
        mv application "$pkgname"
        install -Dm755 ./"$pkgname" "$pkgdir/usr/bin/$pkgname"

}
