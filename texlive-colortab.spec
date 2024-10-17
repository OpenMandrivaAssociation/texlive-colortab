Name:		texlive-colortab
Version:	22155
Release:	2
Summary:	Shade cells of tables and halign
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/colortab
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/colortab.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/colortab.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Lets you shade or colour the cells in the alignment
environments such as \halign and LaTeX's tabular and array
environments. The colortbl or package is to be preferred today
with LaTeX (it assures compatibility with the longtable
package, which is no longer true with colortab); another modern
option is the table-colouring option of the xcolor. However,
colortab remains an adequate solution for use with Plain TeX.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/colortab/colortab.sty
%{_texmfdistdir}/tex/generic/colortab/colortab.tex
%doc %{_texmfdistdir}/doc/generic/colortab/Changes
%doc %{_texmfdistdir}/doc/generic/colortab/Makefile
%doc %{_texmfdistdir}/doc/generic/colortab/colortab-doc.pdf
%doc %{_texmfdistdir}/doc/generic/colortab/colortab-doc.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
