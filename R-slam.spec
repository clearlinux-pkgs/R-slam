#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-slam
Version  : 0.1.50
Release  : 57
URL      : https://cran.r-project.org/src/contrib/slam_0.1-50.tar.gz
Source0  : https://cran.r-project.org/src/contrib/slam_0.1-50.tar.gz
Summary  : Sparse Lightweight Arrays and Matrices
Group    : Development/Tools
License  : GPL-2.0
Requires: R-slam-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
based on index arrays and simple triplet representations, respectively.

%package lib
Summary: lib components for the R-slam package.
Group: Libraries

%description lib
lib components for the R-slam package.


%prep
%setup -q -c -n slam
cd %{_builddir}/slam

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641951995

%install
export SOURCE_DATE_EPOCH=1641951995
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library slam
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library slam
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library slam
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc slam || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/slam/DESCRIPTION
/usr/lib64/R/library/slam/INDEX
/usr/lib64/R/library/slam/Meta/Rd.rds
/usr/lib64/R/library/slam/Meta/features.rds
/usr/lib64/R/library/slam/Meta/hsearch.rds
/usr/lib64/R/library/slam/Meta/links.rds
/usr/lib64/R/library/slam/Meta/nsInfo.rds
/usr/lib64/R/library/slam/Meta/package.rds
/usr/lib64/R/library/slam/NAMESPACE
/usr/lib64/R/library/slam/R/slam
/usr/lib64/R/library/slam/R/slam.rdb
/usr/lib64/R/library/slam/R/slam.rdx
/usr/lib64/R/library/slam/help/AnIndex
/usr/lib64/R/library/slam/help/aliases.rds
/usr/lib64/R/library/slam/help/paths.rds
/usr/lib64/R/library/slam/help/slam.rdb
/usr/lib64/R/library/slam/help/slam.rdx
/usr/lib64/R/library/slam/html/00Index.html
/usr/lib64/R/library/slam/html/R.css
/usr/lib64/R/library/slam/po/en@quot/LC_MESSAGES/R-slam.mo
/usr/lib64/R/library/slam/tests/abind.R
/usr/lib64/R/library/slam/tests/abind.Rout.save
/usr/lib64/R/library/slam/tests/apply.R
/usr/lib64/R/library/slam/tests/apply.Rout.save
/usr/lib64/R/library/slam/tests/crossprod.R
/usr/lib64/R/library/slam/tests/crossprod.Rout.save
/usr/lib64/R/library/slam/tests/dimgets.R
/usr/lib64/R/library/slam/tests/extract.R
/usr/lib64/R/library/slam/tests/extract.Rout.save
/usr/lib64/R/library/slam/tests/matrix.R
/usr/lib64/R/library/slam/tests/matrix.Rout.save
/usr/lib64/R/library/slam/tests/matrix_dimnames.R
/usr/lib64/R/library/slam/tests/matrix_dimnames.Rout.save
/usr/lib64/R/library/slam/tests/rollup.R
/usr/lib64/R/library/slam/tests/rollup.Rout.save
/usr/lib64/R/library/slam/tests/split.R
/usr/lib64/R/library/slam/tests/split.Rout.save
/usr/lib64/R/library/slam/tests/ssa_valid.R
/usr/lib64/R/library/slam/tests/ssa_valid.Rout.save
/usr/lib64/R/library/slam/tests/stm.R
/usr/lib64/R/library/slam/tests/stm.Rout.save
/usr/lib64/R/library/slam/tests/stm_apply.R
/usr/lib64/R/library/slam/tests/stm_apply.Rout.save
/usr/lib64/R/library/slam/tests/stm_rollup.R
/usr/lib64/R/library/slam/tests/stm_rollup.Rout.save
/usr/lib64/R/library/slam/tests/stm_subassign.R
/usr/lib64/R/library/slam/tests/stm_subassign.Rout.save
/usr/lib64/R/library/slam/tests/stm_ttcrossprod.R
/usr/lib64/R/library/slam/tests/stm_ttcrossprod.Rout.save
/usr/lib64/R/library/slam/tests/stm_valid.R
/usr/lib64/R/library/slam/tests/stm_valid.Rout.save
/usr/lib64/R/library/slam/tests/stm_zeros.R
/usr/lib64/R/library/slam/tests/stm_zeros.Rout.save
/usr/lib64/R/library/slam/tests/subassign.R
/usr/lib64/R/library/slam/tests/subassign.Rout.save
/usr/lib64/R/library/slam/tests/util.R
/usr/lib64/R/library/slam/tests/util.Rout.save

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/slam/libs/slam.so
/usr/lib64/R/library/slam/libs/slam.so.avx2
/usr/lib64/R/library/slam/libs/slam.so.avx512
