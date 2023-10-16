# Maintainer: Your Name <your@email.com>
pkgname=my-python-package
pkgver=1.0
pkgrel=1
pkgdesc="Description of your Python package"
arch=("aarch64")
url="https://example.com"
license=("GPL")
depends=("python")

# Use the direct raw URL to the tarball hosted on GitHub
source=("my-python-package.tar.xz::https://github.com/SF-Rocker/Gaia-Web-Browser/raw/main/WebBrowser.tar.xz")

# Add the calculated SHA256 checksum
sha256sums=("e47e29bcdc794006cceb9b284f517e4d52275ed2d30a60733e23fd8079de28de")

package() {
    cd "$srcdir"
    tar -xJf "my-python-package.tar.xz" -C "$pkgdir"
}
