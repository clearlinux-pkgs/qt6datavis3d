#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v4
# autospec commit: da8b975
#
Name     : qt6datavis3d
Version  : 6.6.2
Release  : 9
URL      : https://download.qt.io/official_releases/qt/6.6/6.6.2/submodules/qtdatavis3d-everywhere-src-6.6.2.tar.xz
Source0  : https://download.qt.io/official_releases/qt/6.6/6.6.2/submodules/qtdatavis3d-everywhere-src-6.6.2.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.3 GPL-3.0
Requires: qt6datavis3d-lib = %{version}-%{release}
Requires: qt6datavis3d-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-qt6
BuildRequires : mesa-dev
BuildRequires : qt6base-dev
BuildRequires : qt6declarative-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
---------------------------
Qt Data Visualization 5.9.0
---------------------------

%package dev
Summary: dev components for the qt6datavis3d package.
Group: Development
Requires: qt6datavis3d-lib = %{version}-%{release}
Provides: qt6datavis3d-devel = %{version}-%{release}
Requires: qt6datavis3d = %{version}-%{release}

%description dev
dev components for the qt6datavis3d package.


%package lib
Summary: lib components for the qt6datavis3d package.
Group: Libraries
Requires: qt6datavis3d-license = %{version}-%{release}

%description lib
lib components for the qt6datavis3d package.


%package license
Summary: license components for the qt6datavis3d package.
Group: Default

%description license
license components for the qt6datavis3d package.


%prep
%setup -q -n qtdatavis3d-everywhere-src-6.6.2
cd %{_builddir}/qtdatavis3d-everywhere-src-6.6.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1707946925
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1707946925
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qt6datavis3d
cp %{_builddir}/qtdatavis3d-everywhere-src-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/qt6datavis3d/b073f11f0c81a95ab5e32aa6b5d23a5955a95274 || :
cp %{_builddir}/qtdatavis3d-everywhere-src-%{version}/LICENSES/GFDL-1.3-no-invariants-only.txt %{buildroot}/usr/share/package-licenses/qt6datavis3d/715f995f11805ee85601834220c43b082f457ea3 || :
cp %{_builddir}/qtdatavis3d-everywhere-src-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qt6datavis3d/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/qt6/metatypes/qt6datavisualization_relwithdebinfo_metatypes.json
/usr/lib64/qt6/metatypes/qt6datavisualizationqml_relwithdebinfo_metatypes.json
/usr/lib64/qt6/mkspecs/modules/qt_lib_datavisualization.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_datavisualization_private.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_datavisualizationqml.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_datavisualizationqml_private.pri
/usr/lib64/qt6/modules/DataVisualization.json
/usr/lib64/qt6/modules/DataVisualizationQml.json
/usr/lib64/qt6/qml/QtDataVisualization/designer/Bars3DSpecifics.qml
/usr/lib64/qt6/qml/QtDataVisualization/designer/Scatter3DSpecifics.qml
/usr/lib64/qt6/qml/QtDataVisualization/designer/Surface3DSpecifics.qml
/usr/lib64/qt6/qml/QtDataVisualization/designer/default/Bars3D.qml
/usr/lib64/qt6/qml/QtDataVisualization/designer/default/Scatter3D.qml
/usr/lib64/qt6/qml/QtDataVisualization/designer/default/Surface3D.qml
/usr/lib64/qt6/qml/QtDataVisualization/designer/images/bars3d-icon.png
/usr/lib64/qt6/qml/QtDataVisualization/designer/images/bars3d-icon16.png
/usr/lib64/qt6/qml/QtDataVisualization/designer/images/scatter3d-icon.png
/usr/lib64/qt6/qml/QtDataVisualization/designer/images/scatter3d-icon16.png
/usr/lib64/qt6/qml/QtDataVisualization/designer/images/surface3d-icon.png
/usr/lib64/qt6/qml/QtDataVisualization/designer/images/surface3d-icon16.png
/usr/lib64/qt6/qml/QtDataVisualization/designer/qtdatavisualization.metainfo
/usr/lib64/qt6/qml/QtDataVisualization/plugins.qmltypes
/usr/lib64/qt6/qml/QtDataVisualization/qmldir

%files dev
%defattr(-,root,root,-)
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/abstract3dcontroller_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/abstract3drenderer_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/abstractdeclarativeinterface_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/abstractitemmodelhandler_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/abstractobjecthelper_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/abstractrenderitem_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/axisrendercache_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/baritemmodelhandler_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/barrenderitem_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/bars3dcontroller_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/bars3drenderer_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/barseriesrendercache_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/camerahelper_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/customrenderitem_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/datavisualizationglobal_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/drawer_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/labelitem_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/meshloader_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/objecthelper_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/q3dbars_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/q3dcamera_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/q3dinputhandler_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/q3dlight_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/q3dobject_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/q3dscatter_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/q3dscene_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/q3dsurface_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/q3dtheme_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/qabstract3daxis_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/qabstract3dgraph_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/qabstract3dinputhandler_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/qabstract3dseries_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/qabstractdataproxy_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/qbar3dseries_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/qbardataitem_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/qbardataproxy_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/qcategory3daxis_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/qcustom3ditem_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/qcustom3dlabel_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/qcustom3dvolume_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/qheightmapsurfacedataproxy_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/qitemmodelbardataproxy_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/qitemmodelscatterdataproxy_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/qitemmodelsurfacedataproxy_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/qlogvalue3daxisformatter_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/qscatter3dseries_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/qscatterdataitem_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/qscatterdataproxy_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/qsurface3dseries_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/qsurfacedataitem_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/qsurfacedataproxy_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/qtdatavisualization-config_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/qtouch3dinputhandler_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/qvalue3daxis_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/qvalue3daxisformatter_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/scatter3dcontroller_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/scatter3drenderer_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/scatteritemmodelhandler_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/scatterobjectbufferhelper_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/scatterpointbufferhelper_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/scatterrenderitem_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/scatterseriesrendercache_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/selectionpointer_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/seriesrendercache_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/shaderhelper_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/surface3dcontroller_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/surface3drenderer_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/surfaceitemmodelhandler_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/surfaceobject_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/surfaceseriesrendercache_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/texturehelper_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/thememanager_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/utils_p.h
/usr/include/QtDataVisualization/6.6.2/QtDataVisualization/private/vertexindexer_p.h
/usr/include/QtDataVisualization/Q3DBars
/usr/include/QtDataVisualization/Q3DCamera
/usr/include/QtDataVisualization/Q3DInputHandler
/usr/include/QtDataVisualization/Q3DLight
/usr/include/QtDataVisualization/Q3DObject
/usr/include/QtDataVisualization/Q3DScatter
/usr/include/QtDataVisualization/Q3DScene
/usr/include/QtDataVisualization/Q3DSurface
/usr/include/QtDataVisualization/Q3DTheme
/usr/include/QtDataVisualization/QAbstract3DAxis
/usr/include/QtDataVisualization/QAbstract3DGraph
/usr/include/QtDataVisualization/QAbstract3DInputHandler
/usr/include/QtDataVisualization/QAbstract3DSeries
/usr/include/QtDataVisualization/QAbstractDataProxy
/usr/include/QtDataVisualization/QBar3DSeries
/usr/include/QtDataVisualization/QBarDataArray
/usr/include/QtDataVisualization/QBarDataItem
/usr/include/QtDataVisualization/QBarDataProxy
/usr/include/QtDataVisualization/QBarDataRow
/usr/include/QtDataVisualization/QCategory3DAxis
/usr/include/QtDataVisualization/QCustom3DItem
/usr/include/QtDataVisualization/QCustom3DLabel
/usr/include/QtDataVisualization/QCustom3DVolume
/usr/include/QtDataVisualization/QHeightMapSurfaceDataProxy
/usr/include/QtDataVisualization/QItemModelBarDataProxy
/usr/include/QtDataVisualization/QItemModelScatterDataProxy
/usr/include/QtDataVisualization/QItemModelSurfaceDataProxy
/usr/include/QtDataVisualization/QLogValue3DAxisFormatter
/usr/include/QtDataVisualization/QScatter3DSeries
/usr/include/QtDataVisualization/QScatterDataArray
/usr/include/QtDataVisualization/QScatterDataItem
/usr/include/QtDataVisualization/QScatterDataProxy
/usr/include/QtDataVisualization/QSurface3DSeries
/usr/include/QtDataVisualization/QSurfaceDataArray
/usr/include/QtDataVisualization/QSurfaceDataItem
/usr/include/QtDataVisualization/QSurfaceDataProxy
/usr/include/QtDataVisualization/QSurfaceDataRow
/usr/include/QtDataVisualization/QTouch3DInputHandler
/usr/include/QtDataVisualization/QValue3DAxis
/usr/include/QtDataVisualization/QValue3DAxisFormatter
/usr/include/QtDataVisualization/QtDataVisualization
/usr/include/QtDataVisualization/QtDataVisualizationDepends
/usr/include/QtDataVisualization/QtDataVisualizationVersion
/usr/include/QtDataVisualization/q3dbars.h
/usr/include/QtDataVisualization/q3dcamera.h
/usr/include/QtDataVisualization/q3dinputhandler.h
/usr/include/QtDataVisualization/q3dlight.h
/usr/include/QtDataVisualization/q3dobject.h
/usr/include/QtDataVisualization/q3dscatter.h
/usr/include/QtDataVisualization/q3dscene.h
/usr/include/QtDataVisualization/q3dsurface.h
/usr/include/QtDataVisualization/q3dtheme.h
/usr/include/QtDataVisualization/qabstract3daxis.h
/usr/include/QtDataVisualization/qabstract3dgraph.h
/usr/include/QtDataVisualization/qabstract3dinputhandler.h
/usr/include/QtDataVisualization/qabstract3dseries.h
/usr/include/QtDataVisualization/qabstractdataproxy.h
/usr/include/QtDataVisualization/qbar3dseries.h
/usr/include/QtDataVisualization/qbardataitem.h
/usr/include/QtDataVisualization/qbardataproxy.h
/usr/include/QtDataVisualization/qcategory3daxis.h
/usr/include/QtDataVisualization/qcustom3ditem.h
/usr/include/QtDataVisualization/qcustom3dlabel.h
/usr/include/QtDataVisualization/qcustom3dvolume.h
/usr/include/QtDataVisualization/qdatavisualizationglobal.h
/usr/include/QtDataVisualization/qheightmapsurfacedataproxy.h
/usr/include/QtDataVisualization/qitemmodelbardataproxy.h
/usr/include/QtDataVisualization/qitemmodelscatterdataproxy.h
/usr/include/QtDataVisualization/qitemmodelsurfacedataproxy.h
/usr/include/QtDataVisualization/qlogvalue3daxisformatter.h
/usr/include/QtDataVisualization/qscatter3dseries.h
/usr/include/QtDataVisualization/qscatterdataitem.h
/usr/include/QtDataVisualization/qscatterdataproxy.h
/usr/include/QtDataVisualization/qsurface3dseries.h
/usr/include/QtDataVisualization/qsurfacedataitem.h
/usr/include/QtDataVisualization/qsurfacedataproxy.h
/usr/include/QtDataVisualization/qtdatavisualization-config.h
/usr/include/QtDataVisualization/qtdatavisualizationexports.h
/usr/include/QtDataVisualization/qtdatavisualizationversion.h
/usr/include/QtDataVisualization/qtouch3dinputhandler.h
/usr/include/QtDataVisualization/qutils.h
/usr/include/QtDataVisualization/qvalue3daxis.h
/usr/include/QtDataVisualization/qvalue3daxisformatter.h
/usr/include/QtDataVisualizationQml/6.6.2/QtDataVisualizationQml/private/abstractdeclarative_p.h
/usr/include/QtDataVisualizationQml/6.6.2/QtDataVisualizationQml/private/colorgradient_p.h
/usr/include/QtDataVisualizationQml/6.6.2/QtDataVisualizationQml/private/declarativebars_p.h
/usr/include/QtDataVisualizationQml/6.6.2/QtDataVisualizationQml/private/declarativecolor_p.h
/usr/include/QtDataVisualizationQml/6.6.2/QtDataVisualizationQml/private/declarativerendernode_p.h
/usr/include/QtDataVisualizationQml/6.6.2/QtDataVisualizationQml/private/declarativescatter_p.h
/usr/include/QtDataVisualizationQml/6.6.2/QtDataVisualizationQml/private/declarativescene_p.h
/usr/include/QtDataVisualizationQml/6.6.2/QtDataVisualizationQml/private/declarativeseries_p.h
/usr/include/QtDataVisualizationQml/6.6.2/QtDataVisualizationQml/private/declarativesurface_p.h
/usr/include/QtDataVisualizationQml/6.6.2/QtDataVisualizationQml/private/declarativetheme_p.h
/usr/include/QtDataVisualizationQml/6.6.2/QtDataVisualizationQml/private/enumtostringmap_p.h
/usr/include/QtDataVisualizationQml/6.6.2/QtDataVisualizationQml/private/foreigntypes_p.h
/usr/include/QtDataVisualizationQml/6.6.2/QtDataVisualizationQml/private/glstatestore_p.h
/usr/include/QtDataVisualizationQml/QtDataVisualizationQml
/usr/include/QtDataVisualizationQml/QtDataVisualizationQmlDepends
/usr/include/QtDataVisualizationQml/QtDataVisualizationQmlVersion
/usr/include/QtDataVisualizationQml/qtdatavisualizationqmlversion.h
/usr/lib64/cmake/Qt6BuildInternals/StandaloneTests/QtDataVisualizationTestsConfig.cmake
/usr/lib64/cmake/Qt6DataVisualization/Qt6DataVisualizationAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6DataVisualization/Qt6DataVisualizationConfig.cmake
/usr/lib64/cmake/Qt6DataVisualization/Qt6DataVisualizationConfigVersion.cmake
/usr/lib64/cmake/Qt6DataVisualization/Qt6DataVisualizationConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6DataVisualization/Qt6DataVisualizationDependencies.cmake
/usr/lib64/cmake/Qt6DataVisualization/Qt6DataVisualizationTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6DataVisualization/Qt6DataVisualizationTargets.cmake
/usr/lib64/cmake/Qt6DataVisualization/Qt6DataVisualizationVersionlessTargets.cmake
/usr/lib64/cmake/Qt6DataVisualizationQml/Qt6DataVisualizationQmlAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6DataVisualizationQml/Qt6DataVisualizationQmlConfig.cmake
/usr/lib64/cmake/Qt6DataVisualizationQml/Qt6DataVisualizationQmlConfigVersion.cmake
/usr/lib64/cmake/Qt6DataVisualizationQml/Qt6DataVisualizationQmlConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6DataVisualizationQml/Qt6DataVisualizationQmlDependencies.cmake
/usr/lib64/cmake/Qt6DataVisualizationQml/Qt6DataVisualizationQmlTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6DataVisualizationQml/Qt6DataVisualizationQmlTargets.cmake
/usr/lib64/cmake/Qt6DataVisualizationQml/Qt6DataVisualizationQmlVersionlessTargets.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6DataVisualizationQmlpluginAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6DataVisualizationQmlpluginConfig.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6DataVisualizationQmlpluginConfigVersion.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6DataVisualizationQmlpluginConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6DataVisualizationQmlpluginTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6DataVisualizationQmlpluginTargets.cmake
/usr/lib64/libQt6DataVisualization.prl
/usr/lib64/libQt6DataVisualization.so
/usr/lib64/libQt6DataVisualizationQml.prl
/usr/lib64/libQt6DataVisualizationQml.so
/usr/lib64/pkgconfig/Qt6DataVisualization.pc
/usr/lib64/pkgconfig/Qt6DataVisualizationQml.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libQt6DataVisualization.so.6.6.2
/V3/usr/lib64/libQt6DataVisualizationQml.so.6.6.2
/V3/usr/lib64/qt6/qml/QtDataVisualization/libdatavisualizationqmlplugin.so
/usr/lib64/libQt6DataVisualization.so.6
/usr/lib64/libQt6DataVisualization.so.6.6.2
/usr/lib64/libQt6DataVisualizationQml.so.6
/usr/lib64/libQt6DataVisualizationQml.so.6.6.2
/usr/lib64/qt6/qml/QtDataVisualization/libdatavisualizationqmlplugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qt6datavis3d/715f995f11805ee85601834220c43b082f457ea3
/usr/share/package-licenses/qt6datavis3d/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/qt6datavis3d/b073f11f0c81a95ab5e32aa6b5d23a5955a95274
