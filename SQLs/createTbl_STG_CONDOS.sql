USE [REAL_ESTATE]
GO

/****** Object:  Table [stg].[STG_CONDOS]    Script Date: 2/5/2020 11:26:51 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [stg].[STG_CONDOS](
	[CONDO_NAME] [nvarchar](100) NOT NULL,
	[ADDRESS] [nvarchar](200) NULL,
	[ZIP] [nchar](10) NULL,
	[DISTRICT_ID] [nchar](10) NULL
) ON [PRIMARY]
GO


