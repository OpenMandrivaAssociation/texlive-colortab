# revision 22155
# category Package
# catalog-ctan /macros/generic/colortab
# catalog-date 2010-09-08 11:26:01 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-colortab
Version:	1.0
Release:	1
Summary:	Shade cells of tables and halign
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/colortab
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/colortab.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/colortab.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Lets you shade or colour the cells in the alignment
environments such as \halign and LaTeX's tabular and array
environments. The colortbl or package is to be preferred today
with LaTeX (it assures compatibility with the longtable
package, which is no longer true with colortab); another modern
option is the table-colouring option of the xcolor. However,
colortab remains an adequate solution for use with Plain TeX.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/colortab/colortab.sty
%{_texmfdistdir}/tex/generic/colortab/colortab.tex
%doc %{_texmfdistdir}/doc/generic/colortab/Changes
%doc %{_texmfdistdir}/doc/generic/colortab/Makefile
%doc %{_texmfdistdir}/doc/generic/colortab/colortab-doc.pdf
%doc %{_texmfdistdir}/doc/generic/colortab/colortab-doc.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
