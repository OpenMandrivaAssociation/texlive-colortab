%global tl_name colortab
%global tl_revision 22155

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Shade cells of tables and halign
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/colortab
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/colortab.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/colortab.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package lets you shade or colour the cells in the alignment
environments such as \halign and LaTeX's tabular and array environments.
The colortbl package is to be preferred today with LaTeX (it assures
compatibility with the longtable package, which is no longer true with
colortab); another modern option is the table-colouring option of the
xcolor. However, colortab remains an adequate solution for use with
Plain TeX.

