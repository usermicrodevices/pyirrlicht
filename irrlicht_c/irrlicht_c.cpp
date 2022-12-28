// Copyright(c) Max Kolosov 2010-2022 pyirrlicht@gmail.com
// github.com/usermicrodevices
// BSD license
#include "irrlicht_c.h"

#ifdef _COMPILE_WITH_2DTTFONT_
#ifdef _IRR_WINDOWS_
#ifdef _DEBUG
#pragma comment(lib, "freetype2312MT_D.lib")
#else
#pragma comment(lib, "freetype2312MT.lib")
#endif//_DEBUG
//#else//LINUX not support PRAGMA COMMENT, use -lfreetype2312MT
//#ifdef _DEBUG
//#pragma comment(lib, "freetype2312MT_D.a")
//#else
//#pragma comment(lib, "freetype2312MT.a")
//#endif//_DEBUG
#endif//_IRR_WINDOWS_
#endif//_COMPILE_WITH_2DTTFONT_

#ifdef _COMPILE_WITH_AGG_// || _COMPILE_WITH_IRR_SVG_AGG_
#ifdef _IRR_WINDOWS_
#ifdef _DEBUG
#pragma comment(lib, "libexpatMT_D.lib")
#else//_NDEBUG
#pragma comment(lib, "libexpatMT.lib")
#endif
#else//LINUX
#ifdef _DEBUG
#pragma comment(lib, "libexpatMT_D.a")
#else//_NDEBUG
#pragma comment(lib, "libexpatMT.a")
#endif
#endif
#endif

#ifdef _COMPILE_WITH_IRR_SVG_CAIRO_
#ifdef _IRR_WINDOWS_
#ifdef _DEBUG
#pragma comment(lib, "cairo_d.lib")
#else//_NDEBUG
//#pragma comment(lib, "msimg32.lib")
//#pragma comment(lib, "pixman-1.lib")
//#pragma comment(lib, "cairo-static.lib")
#pragma comment(lib, "cairo.lib")
#endif
#else//LINUX
#ifdef _DEBUG
#pragma comment(lib, "cairo_d.a")
#else
#pragma comment(lib, "cairo.a")
#endif
#endif
#endif

int randrange(int rnd_min = 0, int rnd_max = RAND_MAX)
{
	//return rnd_min+int((rnd_max-rnd_min+1)*rand()/(RAND_MAX + 1.0));
	std::uniform_int_distribution<int> distribution(rnd_min, rnd_max);
	std::default_random_engine generator(std::chrono::system_clock::now().time_since_epoch().count());
	return distribution(generator);
}

IRRLICHT_C_API int tool_randrange(int rnd_min, int rnd_max)
{
	return randrange(rnd_min, rnd_max);
}

IRRLICHT_C_API ITexture* tool_texture_generator(IVideoDriver* driver, video::ECOLOR_FORMAT image_format, const dimension2d<u32>& image_size, const char* texture_name, u32 alpha_value, u32 red1, u32 red2, u32 green1, u32 green2, u32 blue1, u32 blue2)
{
	u32 row, column;
	IImage* image = driver->createImage(image_format, image_size);
	int alpha = 0;
	bool blend = false;
	video::ECOLOR_FORMAT color_format = image->getColorFormat();
	if (color_format == ECF_A1R5G5B5 || color_format == ECF_A8R8G8B8 || color_format == ECF_A16B16G16R16F || color_format == ECF_A32B32G32R32F)
	{
		alpha = alpha_value;
		blend = true;
	}
	srand((unsigned)time(NULL));
	for (row = 0; row < image_size.Height; row++)
	{
		for (column = 0; column < image_size.Width; column++)
			image->setPixel(row, column, SColor(alpha, randrange(red1, red2), randrange(green1, green2), randrange(blue1, blue2)), blend);
	}
	return driver->addTexture(texture_name, image);
}

inline core::array<double> string_split_d(const wchar_t* str, u32 size, const wchar_t* delimiter)
{
	core::array<double> container(size);
	wchar_t* next_token = 0;
	//wchar_t* token = wcstok_s(const_cast<wchar_t*>(str), delimiter, &next_token);
	wchar_t *token = wcstok(const_cast<wchar_t*>(str), delimiter, &next_token);
	int i = 0;
	while (token != NULL)
	{
		container[i] = _wtof(token);
		token = wcstok(NULL, delimiter, &next_token);
		i++;
	}
	return container;
}

//github.com/projectchrono/chrono/blob/main/src/chrono_irrlicht/ChIrrMeshTools.cpp
IRRLICHT_C_API IMesh* tool_createEllipticalMesh(f32 radiusH, f32 radiusV, f32 Ylow, f32 Yhigh, f32 offset, u32 polyCountX, u32 polyCountY)
{
    SMeshBuffer* buffer = new SMeshBuffer();

    // The following code is based on a modified version of the
    // Irrlicht createSphereMesh function, that is also based on the
    // work by Alfaz93
    bool disc_high = false;
    bool disc_low = false;
    if (Yhigh < radiusV)
        disc_high = true;
    if (Ylow > -radiusV)
        disc_low = true;

    if (polyCountX < 2)
        polyCountX = 2;
    if (polyCountY < 2)
        polyCountY = 2;
    if (polyCountX * polyCountY > 32767) {  // prevent u16 overflow
        if (polyCountX > polyCountY)      // prevent u16 overflow
            polyCountX = 32767 / polyCountY - 1;
        else
            polyCountY = 32767 / (polyCountX + 1);
    }

    u32 polyCountXPitch = polyCountX + 1;  // get to same vertex on next level
    u32 n_tot_verts = (polyCountXPitch * polyCountY) + 2;
    u32 n_tot_verts_withoutdiscs = n_tot_verts;
    if (disc_high)
        n_tot_verts += polyCountXPitch;
    if (disc_low)
        n_tot_verts += polyCountXPitch;
    u32 n_tot_indeces = (polyCountX * polyCountY) * 6;
    buffer->Vertices.set_used(n_tot_verts);
    buffer->Indices.set_used(n_tot_indeces);

    irr::video::SColor clr(255, 255, 255, 255);

    u32 i = 0;
    u32 i_disc = 0;
    u32 level = 0;

    for (u32 p1 = 0; p1 < polyCountY - 1; ++p1) {
        // main quads, top to bottom
        for (u32 p2 = 0; p2 < polyCountX - 1; ++p2) {
            const u32 curr = level + p2;
            buffer->Indices[i] = curr + polyCountXPitch;
            buffer->Indices[++i] = curr;
            buffer->Indices[++i] = curr + 1;
            buffer->Indices[++i] = curr + polyCountXPitch;
            buffer->Indices[++i] = curr + 1;
            buffer->Indices[++i] = curr + 1 + polyCountXPitch;
            ++i;
        }

        // the connectors from front to end
        buffer->Indices[i] = level + polyCountX - 1 + polyCountXPitch;
        buffer->Indices[++i] = level + polyCountX - 1;
        buffer->Indices[++i] = level + polyCountX;
        ++i;

        buffer->Indices[i] = level + polyCountX - 1 + polyCountXPitch;
        buffer->Indices[++i] = level + polyCountX;
        buffer->Indices[++i] = level + polyCountX + polyCountXPitch;
        ++i;
        level += polyCountXPitch;
    }

    u32 polyCountSq = polyCountXPitch * polyCountY;          // top point
    u32 polyCountSq1 = polyCountSq + 1;                      // bottom point
    u32 polyCountSqM = 0;                                    // first row's first vertex
    u32 polyCountSqM1 = (polyCountY - 1) * polyCountXPitch;  // last row's first vertex

    if (disc_high && !disc_low)
        polyCountSqM = n_tot_verts_withoutdiscs;
    if (disc_low && !disc_high)
        polyCountSqM1 = n_tot_verts_withoutdiscs;
    if (disc_low && disc_high) {
        polyCountSqM = n_tot_verts_withoutdiscs;
        polyCountSqM1 = polyCountSqM + polyCountX + 1;
    }

    for (u32 p2 = 0; p2 < polyCountX - 1; ++p2) {
        // create triangles which are at the top of the sphere
        buffer->Indices[i] = polyCountSq;
        buffer->Indices[++i] = polyCountSqM + p2 + 1;
        buffer->Indices[++i] = polyCountSqM + p2;
        ++i;

        // create triangles which are at the bottom of the sphere
        buffer->Indices[i] = polyCountSqM1 + p2;
        buffer->Indices[++i] = polyCountSqM1 + p2 + 1;
        buffer->Indices[++i] = polyCountSq1;
        ++i;
    }

    // create final triangle which is at the top of the sphere
    buffer->Indices[i] = polyCountSq;
    buffer->Indices[++i] = polyCountSqM + polyCountX;
    buffer->Indices[++i] = polyCountSqM + polyCountX - 1;
    ++i;

    // create final triangle which is at the bottom of the sphere
    buffer->Indices[i] = polyCountSqM1 + polyCountX - 1;
    buffer->Indices[++i] = polyCountSqM1;
    buffer->Indices[++i] = polyCountSq1;

    // calculate the angle which separates all points in a circle
    f64 r_low, alpha_low, r_high, alpha_high;
    if (disc_high) {
        r_high = radiusH * sqrt(1 - pow(Yhigh / radiusV, 2));
        alpha_high = atan((radiusH / radiusV) * (Yhigh / r_high));
    } else {
        r_high = 0;
        alpha_high = irr::core::PI / 2;
    }

    if (disc_low) {
        r_low = radiusH * sqrt(1 - pow(Ylow / radiusV, 2));
        alpha_low = atan((radiusH / radiusV) * (Ylow / r_low));
    } else {
        r_low = 0;
        alpha_low = -(irr::core::PI / 2);
    }

    const f64 AngleX = 2 * irr::core::PI / polyCountX;
    f64 borderslice = polyCountY;
    if (disc_high)
        borderslice--;
    if (disc_low)
        borderslice--;
    const f64 AngleY = (alpha_high - alpha_low) / borderslice;  //= irr::core::PI / polyCountY;

    i = 0;
    i_disc = n_tot_verts_withoutdiscs;
    f64 axz;

    f64 ay = (irr::core::PI / 2) - alpha_high;  //=0   //=AngleY / 2;  // meant to work in 0..PI, building from top
    if (!disc_high)
        ay += AngleY;

    for (u32 y = 0; y < polyCountY; ++y) {
        const f64 sinay = sin(ay);
        const f64 cosay = cos(ay);
        axz = 0;

        // calculate the necessary vertices without the doubled one
        for (u32 xz = 0; xz < polyCountX; ++xz) {
            // calculate points position

            irr::core::vector3df pos((f32)(radiusH * cos(axz) * sinay), (f32)(radiusV * cosay),
                                     (f32)(radiusH * sin(axz) * sinay));
            // for spheres the normal is the position
            irr::core::vector3df normal(pos);
            normal.normalize();

            // add the offset
            irr::core::vector3df Roffset((f32)(offset * cos(axz)), 0, (f32)(offset * sin(axz)));
            pos += Roffset;

            // calculate texture coordinates via sphere mapping
            // tu is the same on each level, so only calculate once
            f32 tu = 0.5f;
            if (y == 0) {
                if (normal.Y != -1.0f && normal.Y != 1.0f)
                    tu = (f32)(acos(irr::core::clamp(normal.X / sinay, -1.0, 1.0)) * 0.5 * irr::core::RECIPROCAL_PI64);
                if (normal.Z < 0.0f)
                    tu = 1 - tu;
            } else
                tu = buffer->Vertices[i - polyCountXPitch].TCoords.X;

            buffer->Vertices[i] = irr::video::S3DVertex(-pos.X, pos.Y, pos.Z, -normal.X, normal.Y, normal.Z, clr, tu,
                                                        (f32)(ay * irr::core::RECIPROCAL_PI64));
            ++i;

            axz += AngleX;
        }
        // This is the doubled vertex on the initial position
        buffer->Vertices[i] = irr::video::S3DVertex(buffer->Vertices[i - polyCountX]);
        buffer->Vertices[i].TCoords.X = 1.0f;
        ++i;
        ay += AngleY;
    }

    // the vertex at the top of the sphere
    if (disc_high)
        buffer->Vertices[i] = irr::video::S3DVertex(0.0f, Yhigh, 0.0f, 0.0f, 1.0f, 0.0f, clr, 0.5f, 0.0f);
    else
        buffer->Vertices[i] = irr::video::S3DVertex(0.0f, radiusV, 0.0f, 0.0f, 1.0f, 0.0f, clr, 0.5f, 0.0f);

    // the vertex at the bottom of the sphere
    ++i;
    if (disc_low)
        buffer->Vertices[i] = irr::video::S3DVertex(0.0f, Ylow, 0.0f, 0.0f, -1.0f, 0.0f, clr, 0.5f, 1.0f);
    else
        buffer->Vertices[i] = irr::video::S3DVertex(0.0f, -radiusV, 0.0f, 0.0f, -1.0f, 0.0f, clr, 0.5f, 1.0f);

    i_disc = n_tot_verts_withoutdiscs;
    if (disc_high) {
        for (u32 xz = 0; xz < (polyCountX + 1); ++xz) {
            // duplicate points for top disc
            buffer->Vertices[i_disc] = irr::video::S3DVertex(buffer->Vertices[i_disc - n_tot_verts_withoutdiscs]);
            buffer->Vertices[i_disc].Normal.set(0, 1, 0);
            i_disc++;
        }
    }
    int ifrom = 0;
    int mshift = (polyCountY - 1) * polyCountXPitch;  // last row's first vertex
    if (disc_low) {
        for (u32 xz = 0; xz < (polyCountX + 1); ++xz) {
            // duplicate points for low disc
            buffer->Vertices[i_disc] = irr::video::S3DVertex(buffer->Vertices[ifrom + mshift]);
            buffer->Vertices[i_disc].Normal.set(0, -1, 0);
            ifrom++;
            i_disc++;
        }
    }

    // recalculate bounding box

    buffer->BoundingBox.reset(buffer->Vertices[i].Pos);
    buffer->BoundingBox.addInternalPoint(buffer->Vertices[i - 1].Pos);
    buffer->BoundingBox.addInternalPoint(radiusH, 0.0f, 0.0f);
    buffer->BoundingBox.addInternalPoint(-radiusH, 0.0f, 0.0f);
    buffer->BoundingBox.addInternalPoint(0.0f, 0.0f, radiusH);
    buffer->BoundingBox.addInternalPoint(0.0f, 0.0f, -radiusH);

    SMesh* mmesh = new SMesh();
    mmesh->addMeshBuffer(buffer);
    mmesh->recalculateBoundingBox();
    buffer->drop();
    return mmesh;
}
