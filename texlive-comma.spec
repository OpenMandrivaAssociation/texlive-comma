Name:		texlive-comma
Version:	18259
Release:	2
Summary:	Formats a number by inserting commas
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/comma
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/comma.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/comma.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A flexible package that allows commas (or anything else) to be
inserted every three digits in a number, as in 1,234.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/comma/comma.sty
%doc %{_texmfdistdir}/doc/latex/comma/README
%doc %{_texmfdistdir}/doc/latex/comma/comma.pdf
%doc %{_texmfdistdir}/doc/latex/comma/comma.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
