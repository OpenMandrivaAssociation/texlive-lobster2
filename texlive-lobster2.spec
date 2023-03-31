Name:		texlive-lobster2
Version:	64442
Release:	2
Summary:	Lobster Two fonts, with support for all LaTeX engines
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/lobster2
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lobster2.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lobster2.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Lobster Two is a family of script fonts designed bt Pablo
Impallari. It has many ligatures and terminal forms, but most
of these can be accessed only using XeLaTeX or LuaLaTeX. Font
access and use is supported in LaTeX.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/enc/dvips/lobster2
%{_texmfdistdir}/fonts/map/dvips/lobster2
%{_texmfdistdir}/fonts/opentype/impallari/lobster2
%{_texmfdistdir}/fonts/tfm/impallari/lobster2
%{_texmfdistdir}/fonts/type1/impallari/lobster2
%{_texmfdistdir}/fonts/vf/impallari/lobster2
%{_texmfdistdir}/tex/latex/lobster2
%doc %{_texmfdistdir}/doc/fonts/lobster2

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
