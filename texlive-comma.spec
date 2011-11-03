# revision 18259
# category Package
# catalog-ctan /macros/latex/contrib/comma
# catalog-date 2010-05-23 19:54:42 +0200
# catalog-license lppl
# catalog-version 1.2
Name:		texlive-comma
Version:	1.2
Release:	1
Summary:	Formats a number by inserting commas
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/comma
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/comma.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/comma.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A flexible package that allows commas (or anything else) to be
inserted every three digits in a number, as in 1,234.

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
%{_texmfdistdir}/tex/latex/comma/comma.sty
%doc %{_texmfdistdir}/doc/latex/comma/README
%doc %{_texmfdistdir}/doc/latex/comma/comma.pdf
%doc %{_texmfdistdir}/doc/latex/comma/comma.tex
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
