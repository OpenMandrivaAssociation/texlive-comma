# revision 18259
# category Package
# catalog-ctan /macros/latex/contrib/comma
# catalog-date 2010-05-23 19:54:42 +0200
# catalog-license lppl
# catalog-version 1.2
Name:		texlive-comma
Version:	1.2
Release:	3
Summary:	Formats a number by inserting commas
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/comma
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/comma.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/comma.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.2-2
+ Revision: 750407
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.2-1
+ Revision: 718107
- texlive-comma
- texlive-comma
- texlive-comma
- texlive-comma

