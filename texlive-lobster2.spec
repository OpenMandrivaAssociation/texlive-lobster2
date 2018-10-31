# revision 32617
# category Package
# catalog-ctan /fonts/lobster2
# catalog-date 2014-01-10 00:00:21 +0100
# catalog-license ofl
# catalog-version undef
Name:		texlive-lobster2
Version:	20180303
Release:	2
Summary:	Lobster Two fonts, with support for all LaTeX engines
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/lobster2
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lobster2.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lobster2.doc.tar.xz
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
%{_texmfdistdir}/fonts/enc/dvips/lobster2/lbst2_2vl4dw.enc
%{_texmfdistdir}/fonts/enc/dvips/lobster2/lbst2_5uiiua.enc
%{_texmfdistdir}/fonts/enc/dvips/lobster2/lbst2_lyobxw.enc
%{_texmfdistdir}/fonts/enc/dvips/lobster2/lbst2_xn7u5r.enc
%{_texmfdistdir}/fonts/map/dvips/lobster2/LobsterTwo.map
%{_texmfdistdir}/fonts/opentype/impallari/lobster2/LobsterTwo-Bold.otf
%{_texmfdistdir}/fonts/opentype/impallari/lobster2/LobsterTwo-BoldItalic.otf
%{_texmfdistdir}/fonts/opentype/impallari/lobster2/LobsterTwo-Italic.otf
%{_texmfdistdir}/fonts/opentype/impallari/lobster2/LobsterTwo-Regular.otf
%{_texmfdistdir}/fonts/tfm/impallari/lobster2/LobsterTwo-Bold-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/lobster2/LobsterTwo-Bold-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/lobster2/LobsterTwo-Bold-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/lobster2/LobsterTwo-Bold-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/lobster2/LobsterTwo-Bold-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/lobster2/LobsterTwo-Bold-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/lobster2/LobsterTwo-Bold-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/lobster2/LobsterTwo-Bold-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/lobster2/LobsterTwo-Bold-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/lobster2/LobsterTwo-Bold-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/lobster2/LobsterTwo-Bold-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/lobster2/LobsterTwo-BoldItalic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/lobster2/LobsterTwo-BoldItalic-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/lobster2/LobsterTwo-BoldItalic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/lobster2/LobsterTwo-BoldItalic-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/lobster2/LobsterTwo-BoldItalic-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/lobster2/LobsterTwo-BoldItalic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/lobster2/LobsterTwo-BoldItalic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/lobster2/LobsterTwo-BoldItalic-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/lobster2/LobsterTwo-BoldItalic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/lobster2/LobsterTwo-BoldItalic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/lobster2/LobsterTwo-BoldItalic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/lobster2/LobsterTwo-Italic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/lobster2/LobsterTwo-Italic-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/lobster2/LobsterTwo-Italic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/lobster2/LobsterTwo-Italic-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/lobster2/LobsterTwo-Italic-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/lobster2/LobsterTwo-Italic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/lobster2/LobsterTwo-Italic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/lobster2/LobsterTwo-Italic-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/lobster2/LobsterTwo-Italic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/lobster2/LobsterTwo-Italic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/lobster2/LobsterTwo-Italic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/lobster2/LobsterTwo-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/lobster2/LobsterTwo-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/lobster2/LobsterTwo-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/lobster2/LobsterTwo-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/lobster2/LobsterTwo-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/lobster2/LobsterTwo-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/lobster2/LobsterTwo-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/lobster2/LobsterTwo-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/lobster2/LobsterTwo-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/lobster2/LobsterTwo-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/lobster2/LobsterTwo-lf-ts1.tfm
%{_texmfdistdir}/fonts/truetype/impallari/lobster2/LobsterTwo-Bold.ttf
%{_texmfdistdir}/fonts/truetype/impallari/lobster2/LobsterTwo-BoldItalic.ttf
%{_texmfdistdir}/fonts/truetype/impallari/lobster2/LobsterTwo-Italic.ttf
%{_texmfdistdir}/fonts/truetype/impallari/lobster2/LobsterTwo-Regular.ttf
%{_texmfdistdir}/fonts/type1/impallari/lobster2/LobsterTwo-Bold.pfb
%{_texmfdistdir}/fonts/type1/impallari/lobster2/LobsterTwo-BoldItalic.pfb
%{_texmfdistdir}/fonts/type1/impallari/lobster2/LobsterTwo-BoldItalicLCDFJ.pfb
%{_texmfdistdir}/fonts/type1/impallari/lobster2/LobsterTwo-BoldLCDFJ.pfb
%{_texmfdistdir}/fonts/type1/impallari/lobster2/LobsterTwo-Italic.pfb
%{_texmfdistdir}/fonts/type1/impallari/lobster2/LobsterTwo-ItalicLCDFJ.pfb
%{_texmfdistdir}/fonts/type1/impallari/lobster2/LobsterTwo.pfb
%{_texmfdistdir}/fonts/type1/impallari/lobster2/LobsterTwoLCDFJ.pfb
%{_texmfdistdir}/fonts/vf/impallari/lobster2/LobsterTwo-Bold-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/lobster2/LobsterTwo-Bold-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/lobster2/LobsterTwo-Bold-lf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/lobster2/LobsterTwo-Bold-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/lobster2/LobsterTwo-BoldItalic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/lobster2/LobsterTwo-BoldItalic-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/lobster2/LobsterTwo-BoldItalic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/lobster2/LobsterTwo-BoldItalic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/lobster2/LobsterTwo-Italic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/lobster2/LobsterTwo-Italic-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/lobster2/LobsterTwo-Italic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/lobster2/LobsterTwo-Italic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/lobster2/LobsterTwo-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/lobster2/LobsterTwo-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/lobster2/LobsterTwo-lf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/lobster2/LobsterTwo-lf-ts1.vf
%{_texmfdistdir}/tex/latex/lobster2/LY1LobsterTwo-LF.fd
%{_texmfdistdir}/tex/latex/lobster2/LobsterTwo.sty
%{_texmfdistdir}/tex/latex/lobster2/OT1LobsterTwo-LF.fd
%{_texmfdistdir}/tex/latex/lobster2/T1LobsterTwo-LF.fd
%{_texmfdistdir}/tex/latex/lobster2/TS1LobsterTwo-LF.fd
%doc %{_texmfdistdir}/doc/fonts/lobster2/OFL.txt
%doc %{_texmfdistdir}/doc/fonts/lobster2/README
%doc %{_texmfdistdir}/doc/fonts/lobster2/lobster2-samples.pdf
%doc %{_texmfdistdir}/doc/fonts/lobster2/lobster2-samples.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
