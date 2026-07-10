%global tl_name comma
%global tl_revision 78931

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	Formats a number by inserting commas
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/comma
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/comma.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/comma.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A flexible package that allows commas (or anything else) to be inserted
every three digits in a number, as in 1,234.

