/* A Bison parser, made by GNU Bison 2.7.  */

/* Bison implementation for Yacc-like parsers in C
   
      Copyright (C) 1984, 1989-1990, 2000-2012 Free Software Foundation, Inc.
   
   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.
   
   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
   
   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.
   
   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* C LALR(1) parser skeleton written by Richard Stallman, by
   simplifying the original so-called "semantic" parser.  */

/* All symbols defined below should begin with yy or YY, to avoid
   infringing on user name space.  This should be done even for local
   variables, as they might otherwise be expanded by user macros.
   There are some unavoidable exceptions within include files to
   define necessary library symbols; they are noted "INFRINGES ON
   USER NAME SPACE" below.  */

/* Identify Bison output.  */
#define YYBISON 1

/* Bison version.  */
#define YYBISON_VERSION "2.7"

/* Skeleton name.  */
#define YYSKELETON_NAME "yacc.c"

/* Pure parsers.  */
#define YYPURE 0

/* Push parsers.  */
#define YYPUSH 0

/* Pull parsers.  */
#define YYPULL 1


/* Substitute the variable and function names.  */
#define yyparse         vrmlyyparse
#define yylex           vrmlyylex
#define yyerror         vrmlyyerror
#define yylval          vrmlyylval
#define yychar          vrmlyychar
#define yydebug         vrmlyydebug
#define yynerrs         vrmlyynerrs

/* Copy the first part of user declarations.  */
/* Line 371 of yacc.c  */
#line 22 "pandatool/src/vrml/vrmlParser.yxx"


//
// Parser for VRML 2.0 files.
// This is a minimal parser that does NOT generate an in-memory scene graph.
// 

// The original parser was developed on a Windows 95 PC with
// Borland's C++ 5.0 development tools.  This was then ported
// to a Windows 95 PC with Microsoft's MSDEV C++ 4.0 development
// tools.  The port introduced the ifdef's for
//    USING_BORLAND_CPP_5          : since this provides a "std namespace",
//    TWO_ARGUMENTS_FOR_STL_STACK  : STL is a moving target.  The stack template
//                                     class takes either one or two arguments.

#include "pandatoolbase.h"
#include "vrmlLexerDefs.h"
#include "vrmlNodeType.h"
#include "vrmlNode.h"
#include "pnotify.h"
#include "plist.h"

#include <stack>
#include <stdio.h>  // for sprintf()

//#define YYDEBUG 1

// Currently-being-define proto.  Prototypes may be nested, so a stack
// is needed:

stack< VrmlNodeType*, plist<VrmlNodeType*> > currentProtoStack;

// This is used to keep track of which field in which type of node is being
// parsed.  Field are nested (nodes are contained inside MFNode/SFNode fields)
// so a stack of these is needed:
typedef struct {
    const VrmlNodeType *nodeType;
    const char *fieldName;
    const VrmlNodeType::NameTypeRec *typeRec;
} FieldRec;

stack< FieldRec*, plist<FieldRec*> > currentField;

// Similarly for the node entries (which contain the actual values for
// the fields as they are encountered):

stack< VrmlNode*, plist<VrmlNode*> > currentNode;

// This is used when the parser knows what kind of token it expects
// to get next-- used when parsing field values (whose types are declared
// and read by the parser) and at certain other places:
extern int expectToken;

// This is where we store the parsed scene.
VrmlScene *parsed_scene = NULL;

// Some helper routines defined below:
static void beginProto(const char *);
static void endProto();
int addField(const char *type, const char *name, const VrmlFieldValue *dflt = NULL);
int addEventIn(const char *type, const char *name, const VrmlFieldValue *dflt = NULL);
int addEventOut(const char *type, const char *name, const VrmlFieldValue *dflt = NULL);
int addExposedField(const char *type, const char *name, const VrmlFieldValue *dflt = NULL);
int add(void (VrmlNodeType::*func)(const char *, int, const VrmlFieldValue *), 
        const char *typeString, const char *name,
        const VrmlFieldValue *dflt);
int fieldType(const char *type);
void enterNode(const char *);
VrmlNode *exitNode();
void inScript();
void enterField(const char *);
void storeField(const VrmlFieldValue &value);
void exitField();
void expect(int type);

extern void vrmlyyerror(const string &);

////////////////////////////////////////////////////////////////////
// Defining the interface to the parser.
////////////////////////////////////////////////////////////////////

void
vrml_init_parser(istream &in, const string &filename) {
  //yydebug = 0;
  vrml_init_lexer(in, filename);
}

void
vrml_cleanup_parser() {
}


/* Line 371 of yacc.c  */
#line 168 "built/tmp/vrmlParser.yxx.c"

# ifndef YY_NULL
#  if defined __cplusplus && 201103L <= __cplusplus
#   define YY_NULL nullptr
#  else
#   define YY_NULL 0
#  endif
# endif

/* Enabling verbose error messages.  */
#ifdef YYERROR_VERBOSE
# undef YYERROR_VERBOSE
# define YYERROR_VERBOSE 1
#else
# define YYERROR_VERBOSE 0
#endif

/* In a future release of Bison, this section will be replaced
   by #include "vrmlParser.yxx.h".  */
#ifndef YY_VRMLYY_BUILT_TMP_VRMLPARSER_YXX_H_INCLUDED
# define YY_VRMLYY_BUILT_TMP_VRMLPARSER_YXX_H_INCLUDED
/* Enabling traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int vrmlyydebug;
#endif

/* Tokens.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
   /* Put the tokens into the symbol table, so that GDB and other debuggers
      know about them.  */
   enum yytokentype {
     IDENTIFIER = 258,
     DEF = 259,
     USE = 260,
     PROTO = 261,
     EXTERNPROTO = 262,
     TO = 263,
     IS = 264,
     ROUTE = 265,
     SFN_NULL = 266,
     EVENTIN = 267,
     EVENTOUT = 268,
     FIELD = 269,
     EXPOSEDFIELD = 270,
     SFBOOL = 271,
     SFCOLOR = 272,
     SFFLOAT = 273,
     SFIMAGE = 274,
     SFINT32 = 275,
     SFNODE = 276,
     SFROTATION = 277,
     SFSTRING = 278,
     SFTIME = 279,
     SFVEC2F = 280,
     SFVEC3F = 281,
     MFCOLOR = 282,
     MFFLOAT = 283,
     MFINT32 = 284,
     MFROTATION = 285,
     MFSTRING = 286,
     MFVEC2F = 287,
     MFVEC3F = 288,
     MFNODE = 289
   };
#endif
/* Tokens.  */
#define IDENTIFIER 258
#define DEF 259
#define USE 260
#define PROTO 261
#define EXTERNPROTO 262
#define TO 263
#define IS 264
#define ROUTE 265
#define SFN_NULL 266
#define EVENTIN 267
#define EVENTOUT 268
#define FIELD 269
#define EXPOSEDFIELD 270
#define SFBOOL 271
#define SFCOLOR 272
#define SFFLOAT 273
#define SFIMAGE 274
#define SFINT32 275
#define SFNODE 276
#define SFROTATION 277
#define SFSTRING 278
#define SFTIME 279
#define SFVEC2F 280
#define SFVEC3F 281
#define MFCOLOR 282
#define MFFLOAT 283
#define MFINT32 284
#define MFROTATION 285
#define MFSTRING 286
#define MFVEC2F 287
#define MFVEC3F 288
#define MFNODE 289



#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef union YYSTYPE
{
/* Line 387 of yacc.c  */
#line 115 "pandatool/src/vrml/vrmlParser.yxx"

  char *string;
  VrmlFieldValue fv;
  VrmlNode *node;
  MFArray *mfarray;
  SFNodeRef nodeRef;
  VrmlScene *scene;


/* Line 387 of yacc.c  */
#line 289 "built/tmp/vrmlParser.yxx.c"
} YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
#endif

extern YYSTYPE vrmlyylval;

#ifdef YYPARSE_PARAM
#if defined __STDC__ || defined __cplusplus
int vrmlyyparse (void *YYPARSE_PARAM);
#else
int vrmlyyparse ();
#endif
#else /* ! YYPARSE_PARAM */
#if defined __STDC__ || defined __cplusplus
int vrmlyyparse (void);
#else
int vrmlyyparse ();
#endif
#endif /* ! YYPARSE_PARAM */

#endif /* !YY_VRMLYY_BUILT_TMP_VRMLPARSER_YXX_H_INCLUDED  */

/* Copy the second part of user declarations.  */

/* Line 390 of yacc.c  */
#line 317 "built/tmp/vrmlParser.yxx.c"

#ifdef short
# undef short
#endif

#ifdef YYTYPE_UINT8
typedef YYTYPE_UINT8 yytype_uint8;
#else
typedef unsigned char yytype_uint8;
#endif

#ifdef YYTYPE_INT8
typedef YYTYPE_INT8 yytype_int8;
#elif (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
typedef signed char yytype_int8;
#else
typedef short int yytype_int8;
#endif

#ifdef YYTYPE_UINT16
typedef YYTYPE_UINT16 yytype_uint16;
#else
typedef unsigned short int yytype_uint16;
#endif

#ifdef YYTYPE_INT16
typedef YYTYPE_INT16 yytype_int16;
#else
typedef short int yytype_int16;
#endif

#ifndef YYSIZE_T
# ifdef __SIZE_TYPE__
#  define YYSIZE_T __SIZE_TYPE__
# elif defined size_t
#  define YYSIZE_T size_t
# elif ! defined YYSIZE_T && (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
#  include <stddef.h> /* INFRINGES ON USER NAME SPACE */
#  define YYSIZE_T size_t
# else
#  define YYSIZE_T unsigned int
# endif
#endif

#define YYSIZE_MAXIMUM ((YYSIZE_T) -1)

#ifndef YY_
# if defined YYENABLE_NLS && YYENABLE_NLS
#  if ENABLE_NLS
#   include <libintl.h> /* INFRINGES ON USER NAME SPACE */
#   define YY_(Msgid) dgettext ("bison-runtime", Msgid)
#  endif
# endif
# ifndef YY_
#  define YY_(Msgid) Msgid
# endif
#endif

/* Suppress unused-variable warnings by "using" E.  */
#if ! defined lint || defined __GNUC__
# define YYUSE(E) ((void) (E))
#else
# define YYUSE(E) /* empty */
#endif

/* Identity function, used to suppress warnings about constant conditions.  */
#ifndef lint
# define YYID(N) (N)
#else
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static int
YYID (int yyi)
#else
static int
YYID (yyi)
    int yyi;
#endif
{
  return yyi;
}
#endif

#if ! defined yyoverflow || YYERROR_VERBOSE

/* The parser invokes alloca or malloc; define the necessary symbols.  */

# ifdef YYSTACK_USE_ALLOCA
#  if YYSTACK_USE_ALLOCA
#   ifdef __GNUC__
#    define YYSTACK_ALLOC __builtin_alloca
#   elif defined __BUILTIN_VA_ARG_INCR
#    include <alloca.h> /* INFRINGES ON USER NAME SPACE */
#   elif defined _AIX
#    define YYSTACK_ALLOC __alloca
#   elif defined _MSC_VER
#    include <malloc.h> /* INFRINGES ON USER NAME SPACE */
#    define alloca _alloca
#   else
#    define YYSTACK_ALLOC alloca
#    if ! defined _ALLOCA_H && ! defined EXIT_SUCCESS && (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
#     include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
      /* Use EXIT_SUCCESS as a witness for stdlib.h.  */
#     ifndef EXIT_SUCCESS
#      define EXIT_SUCCESS 0
#     endif
#    endif
#   endif
#  endif
# endif

# ifdef YYSTACK_ALLOC
   /* Pacify GCC's `empty if-body' warning.  */
#  define YYSTACK_FREE(Ptr) do { /* empty */; } while (YYID (0))
#  ifndef YYSTACK_ALLOC_MAXIMUM
    /* The OS might guarantee only one guard page at the bottom of the stack,
       and a page size can be as small as 4096 bytes.  So we cannot safely
       invoke alloca (N) if N exceeds 4096.  Use a slightly smaller number
       to allow for a few compiler-allocated temporary stack slots.  */
#   define YYSTACK_ALLOC_MAXIMUM 4032 /* reasonable circa 2006 */
#  endif
# else
#  define YYSTACK_ALLOC YYMALLOC
#  define YYSTACK_FREE YYFREE
#  ifndef YYSTACK_ALLOC_MAXIMUM
#   define YYSTACK_ALLOC_MAXIMUM YYSIZE_MAXIMUM
#  endif
#  if (defined __cplusplus && ! defined EXIT_SUCCESS \
       && ! ((defined YYMALLOC || defined malloc) \
	     && (defined YYFREE || defined free)))
#   include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
#   ifndef EXIT_SUCCESS
#    define EXIT_SUCCESS 0
#   endif
#  endif
#  ifndef YYMALLOC
#   define YYMALLOC malloc
#   if ! defined malloc && ! defined EXIT_SUCCESS && (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
void *malloc (YYSIZE_T); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
#  ifndef YYFREE
#   define YYFREE free
#   if ! defined free && ! defined EXIT_SUCCESS && (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
void free (void *); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
# endif
#endif /* ! defined yyoverflow || YYERROR_VERBOSE */


#if (! defined yyoverflow \
     && (! defined __cplusplus \
	 || (defined YYSTYPE_IS_TRIVIAL && YYSTYPE_IS_TRIVIAL)))

/* A type that is properly aligned for any stack member.  */
union yyalloc
{
  yytype_int16 yyss_alloc;
  YYSTYPE yyvs_alloc;
};

/* The size of the maximum gap between one aligned stack and the next.  */
# define YYSTACK_GAP_MAXIMUM (sizeof (union yyalloc) - 1)

/* The size of an array large to enough to hold all stacks, each with
   N elements.  */
# define YYSTACK_BYTES(N) \
     ((N) * (sizeof (yytype_int16) + sizeof (YYSTYPE)) \
      + YYSTACK_GAP_MAXIMUM)

# define YYCOPY_NEEDED 1

/* Relocate STACK from its old location to the new one.  The
   local variables YYSIZE and YYSTACKSIZE give the old and new number of
   elements in the stack, and YYPTR gives the new location of the
   stack.  Advance YYPTR to a properly aligned location for the next
   stack.  */
# define YYSTACK_RELOCATE(Stack_alloc, Stack)				\
    do									\
      {									\
	YYSIZE_T yynewbytes;						\
	YYCOPY (&yyptr->Stack_alloc, Stack, yysize);			\
	Stack = &yyptr->Stack_alloc;					\
	yynewbytes = yystacksize * sizeof (*Stack) + YYSTACK_GAP_MAXIMUM; \
	yyptr += yynewbytes / sizeof (*yyptr);				\
      }									\
    while (YYID (0))

#endif

#if defined YYCOPY_NEEDED && YYCOPY_NEEDED
/* Copy COUNT objects from SRC to DST.  The source and destination do
   not overlap.  */
# ifndef YYCOPY
#  if defined __GNUC__ && 1 < __GNUC__
#   define YYCOPY(Dst, Src, Count) \
      __builtin_memcpy (Dst, Src, (Count) * sizeof (*(Src)))
#  else
#   define YYCOPY(Dst, Src, Count)              \
      do                                        \
        {                                       \
          YYSIZE_T yyi;                         \
          for (yyi = 0; yyi < (Count); yyi++)   \
            (Dst)[yyi] = (Src)[yyi];            \
        }                                       \
      while (YYID (0))
#  endif
# endif
#endif /* !YYCOPY_NEEDED */

/* YYFINAL -- State number of the termination state.  */
#define YYFINAL  3
/* YYLAST -- Last index in YYTABLE.  */
#define YYLAST   126

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  40
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  26
/* YYNRULES -- Number of rules.  */
#define YYNRULES  70
/* YYNRULES -- Number of states.  */
#define YYNSTATES  125

/* YYTRANSLATE(YYLEX) -- Bison symbol number corresponding to YYLEX.  */
#define YYUNDEFTOK  2
#define YYMAXUTOK   289

#define YYTRANSLATE(YYX)						\
  ((unsigned int) (YYX) <= YYMAXUTOK ? yytranslate[YYX] : YYUNDEFTOK)

/* YYTRANSLATE[YYLEX] -- Bison symbol number corresponding to YYLEX.  */
static const yytype_uint8 yytranslate[] =
{
       0,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,    39,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,    35,     2,    36,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,    37,     2,    38,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     1,     2,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    12,    13,    14,
      15,    16,    17,    18,    19,    20,    21,    22,    23,    24,
      25,    26,    27,    28,    29,    30,    31,    32,    33,    34
};

#if YYDEBUG
/* YYPRHS[YYN] -- Index of the first RHS symbol of rule number YYN in
   YYRHS.  */
static const yytype_uint8 yyprhs[] =
{
       0,     0,     3,     5,     6,     9,    12,    15,    17,    21,
      24,    26,    28,    29,    39,    40,    41,    50,    51,    54,
      58,    62,    63,    69,    70,    76,    77,    80,    84,    88,
      92,    96,   105,   106,   112,   113,   116,   117,   121,   123,
     125,   129,   133,   134,   140,   146,   152,   154,   156,   158,
     160,   162,   164,   166,   168,   170,   172,   174,   176,   178,
     180,   182,   184,   186,   189,   192,   195,   198,   202,   204,
     205
};

/* YYRHS -- A `-1'-separated list of the rules' RHS.  */
static const yytype_int8 yyrhs[] =
{
      41,     0,    -1,    42,    -1,    -1,    42,    43,    -1,    42,
      44,    -1,    42,    56,    -1,    57,    -1,     4,     3,    57,
      -1,     5,     3,    -1,    45,    -1,    47,    -1,    -1,     6,
       3,    46,    35,    50,    36,    37,    42,    38,    -1,    -1,
      -1,     7,     3,    48,    35,    54,    36,    49,    63,    -1,
      -1,    50,    51,    -1,    12,     3,     3,    -1,    13,     3,
       3,    -1,    -1,    14,     3,     3,    52,    63,    -1,    -1,
      15,     3,     3,    53,    63,    -1,    -1,    54,    55,    -1,
      12,     3,     3,    -1,    13,     3,     3,    -1,    14,     3,
       3,    -1,    15,     3,     3,    -1,    10,     3,    39,     3,
       8,     3,    39,     3,    -1,    -1,     3,    58,    37,    59,
      38,    -1,    -1,    59,    60,    -1,    -1,     3,    61,    63,
      -1,    56,    -1,    44,    -1,    12,     3,     3,    -1,    13,
       3,     3,    -1,    -1,    14,     3,     3,    62,    63,    -1,
      12,     3,     3,     9,     3,    -1,    13,     3,     3,     9,
       3,    -1,    16,    -1,    17,    -1,    27,    -1,    18,    -1,
      28,    -1,    19,    -1,    20,    -1,    29,    -1,    22,    -1,
      30,    -1,    23,    -1,    31,    -1,    24,    -1,    25,    -1,
      32,    -1,    26,    -1,    33,    -1,    21,    43,    -1,    21,
      11,    -1,    34,    64,    -1,     9,     3,    -1,    35,    65,
      36,    -1,    43,    -1,    -1,    65,    43,    -1
};

/* YYRLINE[YYN] -- source line where rule number YYN was defined.  */
static const yytype_uint16 yyrline[] =
{
       0,   146,   146,   154,   157,   164,   165,   169,   175,   181,
     190,   191,   195,   195,   201,   203,   201,   206,   208,   212,
     214,   217,   216,   228,   227,   240,   242,   246,   248,   250,
     252,   257,   262,   262,   266,   268,   272,   272,   279,   280,
     283,   284,   285,   285,   289,   291,   296,   297,   298,   299,
     300,   301,   302,   303,   304,   305,   306,   307,   308,   309,
     310,   311,   312,   314,   315,   321,   322,   326,   330,   341,
     344
};
#endif

#if YYDEBUG || YYERROR_VERBOSE || 0
/* YYTNAME[SYMBOL-NUM] -- String name of the symbol SYMBOL-NUM.
   First, the terminals, then, starting at YYNTOKENS, nonterminals.  */
static const char *const yytname[] =
{
  "$end", "error", "$undefined", "IDENTIFIER", "DEF", "USE", "PROTO",
  "EXTERNPROTO", "TO", "IS", "ROUTE", "SFN_NULL", "EVENTIN", "EVENTOUT",
  "FIELD", "EXPOSEDFIELD", "SFBOOL", "SFCOLOR", "SFFLOAT", "SFIMAGE",
  "SFINT32", "SFNODE", "SFROTATION", "SFSTRING", "SFTIME", "SFVEC2F",
  "SFVEC3F", "MFCOLOR", "MFFLOAT", "MFINT32", "MFROTATION", "MFSTRING",
  "MFVEC2F", "MFVEC3F", "MFNODE", "'['", "']'", "'{'", "'}'", "'.'",
  "$accept", "vrmlscene", "declarations", "nodeDeclaration",
  "protoDeclaration", "proto", "$@1", "externproto", "$@2", "$@3",
  "interfaceDeclarations", "interfaceDeclaration", "$@4", "$@5",
  "externInterfaceDeclarations", "externInterfaceDeclaration",
  "routeDeclaration", "node", "$@6", "nodeGuts", "nodeGut", "$@7", "$@8",
  "fieldValue", "mfnodeValue", "nodes", YY_NULL
};
#endif

# ifdef YYPRINT
/* YYTOKNUM[YYLEX-NUM] -- Internal token number corresponding to
   token YYLEX-NUM.  */
static const yytype_uint16 yytoknum[] =
{
       0,   256,   257,   258,   259,   260,   261,   262,   263,   264,
     265,   266,   267,   268,   269,   270,   271,   272,   273,   274,
     275,   276,   277,   278,   279,   280,   281,   282,   283,   284,
     285,   286,   287,   288,   289,    91,    93,   123,   125,    46
};
# endif

/* YYR1[YYN] -- Symbol number of symbol that rule YYN derives.  */
static const yytype_uint8 yyr1[] =
{
       0,    40,    41,    42,    42,    42,    42,    43,    43,    43,
      44,    44,    46,    45,    48,    49,    47,    50,    50,    51,
      51,    52,    51,    53,    51,    54,    54,    55,    55,    55,
      55,    56,    58,    57,    59,    59,    61,    60,    60,    60,
      60,    60,    62,    60,    60,    60,    63,    63,    63,    63,
      63,    63,    63,    63,    63,    63,    63,    63,    63,    63,
      63,    63,    63,    63,    63,    63,    63,    64,    64,    65,
      65
};

/* YYR2[YYN] -- Number of symbols composing right hand side of rule YYN.  */
static const yytype_uint8 yyr2[] =
{
       0,     2,     1,     0,     2,     2,     2,     1,     3,     2,
       1,     1,     0,     9,     0,     0,     8,     0,     2,     3,
       3,     0,     5,     0,     5,     0,     2,     3,     3,     3,
       3,     8,     0,     5,     0,     2,     0,     3,     1,     1,
       3,     3,     0,     5,     5,     5,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     2,     2,     2,     2,     3,     1,     0,
       2
};

/* YYDEFACT[STATE-NAME] -- Default reduction number in state STATE-NUM.
   Performed when YYTABLE doesn't specify something else to do.  Zero
   means the default is an error.  */
static const yytype_uint8 yydefact[] =
{
       3,     0,     2,     1,    32,     0,     0,     0,     0,     0,
       4,     5,    10,    11,     6,     7,     0,     0,     9,    12,
      14,     0,    34,     8,     0,     0,     0,     0,    17,    25,
       0,    36,     0,     0,     0,    33,    39,    38,    35,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    18,     0,     0,     0,     0,    15,    26,     0,     0,
      46,    47,    49,    51,    52,     0,    54,    56,    58,    59,
      61,    48,    50,    53,    55,    57,    60,    62,     0,    37,
      40,    41,    42,     0,     0,     0,     0,     3,     0,     0,
       0,     0,     0,     0,    66,    64,    63,    69,    68,    65,
       0,     0,     0,    19,    20,    21,    23,     0,    27,    28,
      29,    30,    16,    31,     0,    44,    45,    43,     0,     0,
      13,    67,    70,    22,    24
};

/* YYDEFGOTO[NTERM-NUM].  */
static const yytype_int8 yydefgoto[] =
{
      -1,     1,     2,    10,    11,    12,    24,    13,    25,    92,
      39,    51,   118,   119,    40,    57,    14,    15,    16,    27,
      38,    42,   102,    79,    99,   114
};

/* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
   STATE-NUM.  */
#define YYPACT_NINF -73
static const yytype_int8 yypact[] =
{
     -73,     2,    79,   -73,   -73,     0,     3,     4,     6,    11,
     -73,   -73,   -73,   -73,   -73,   -73,   -16,    26,   -73,   -73,
     -73,    -4,   -73,   -73,     5,     7,    38,    -2,   -73,   -73,
      35,   -73,    41,    45,    48,   -73,   -73,   -73,   -73,    19,
      66,    50,    43,    51,    54,    84,    85,    87,    88,    89,
      56,   -73,    91,    92,    93,    94,   -73,   -73,    59,    96,
     -73,   -73,   -73,   -73,   -73,    34,   -73,   -73,   -73,   -73,
     -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,    23,   -73,
      95,    97,   -73,    98,   100,   102,   104,   -73,   105,   106,
     107,   108,    43,   109,   -73,   -73,   -73,   -73,   -73,   -73,
     110,   111,    43,   -73,   -73,   -73,   -73,    12,   -73,   -73,
     -73,   -73,   -73,   -73,    20,   -73,   -73,   -73,    43,    43,
     -73,   -73,   -73,   -73,   -73
};

/* YYPGOTO[NTERM-NUM].  */
static const yytype_int8 yypgoto[] =
{
     -73,   -73,    13,   -65,    90,   -73,   -73,   -73,   -73,   -73,
     -73,   -73,   -73,   -73,   -73,   -73,    99,   101,   -73,   -73,
     -73,   -73,   -73,   -72,   -73,   -73
};

/* YYTABLE[YYPACT[STATE-NUM]].  What to do in state STATE-NUM.  If
   positive, shift that token.  If negative, reduce the rule which
   number is the opposite.  If YYTABLE_NINF, syntax error.  */
#define YYTABLE_NINF -1
static const yytype_uint8 yytable[] =
{
      96,    31,     3,    17,     7,     8,    18,    19,     9,    20,
      32,    33,    34,    98,    21,     4,     5,     6,     7,     8,
     112,    22,     9,     4,     5,     6,     4,     5,     6,     4,
     117,    46,    47,    48,    49,    26,    35,     4,     5,     6,
      28,    30,    29,    41,    43,    95,   123,   124,    44,   122,
     120,    45,    59,    58,    80,    50,   121,    81,    97,    60,
      61,    62,    63,    64,    65,    66,    67,    68,    69,    70,
      71,    72,    73,    74,    75,    76,    77,    78,    52,    53,
      54,    55,     4,     5,     6,     7,     8,    82,    83,     9,
      84,    85,    86,    87,    88,    89,    90,    91,    93,    94,
     107,   103,    56,   104,   100,   105,   101,   106,   108,   109,
     110,   111,   113,   115,   116,     0,     0,    36,    23,     0,
       0,     0,     0,     0,     0,     0,    37
};

#define yypact_value_is_default(Yystate) \
  (!!((Yystate) == (-73)))

#define yytable_value_is_error(Yytable_value) \
  YYID (0)

static const yytype_int8 yycheck[] =
{
      65,     3,     0,     3,     6,     7,     3,     3,    10,     3,
      12,    13,    14,    78,     3,     3,     4,     5,     6,     7,
      92,    37,    10,     3,     4,     5,     3,     4,     5,     3,
     102,    12,    13,    14,    15,    39,    38,     3,     4,     5,
      35,     3,    35,     8,     3,    11,   118,   119,     3,   114,
      38,     3,     9,     3,     3,    36,    36,     3,    35,    16,
      17,    18,    19,    20,    21,    22,    23,    24,    25,    26,
      27,    28,    29,    30,    31,    32,    33,    34,    12,    13,
      14,    15,     3,     4,     5,     6,     7,     3,     3,    10,
       3,     3,     3,    37,     3,     3,     3,     3,    39,     3,
      87,     3,    36,     3,     9,     3,     9,     3,     3,     3,
       3,     3,     3,     3,     3,    -1,    -1,    27,    17,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    27
};

/* YYSTOS[STATE-NUM] -- The (internal number of the) accessing
   symbol of state STATE-NUM.  */
static const yytype_uint8 yystos[] =
{
       0,    41,    42,     0,     3,     4,     5,     6,     7,    10,
      43,    44,    45,    47,    56,    57,    58,     3,     3,     3,
       3,     3,    37,    57,    46,    48,    39,    59,    35,    35,
       3,     3,    12,    13,    14,    38,    44,    56,    60,    50,
      54,     8,    61,     3,     3,     3,    12,    13,    14,    15,
      36,    51,    12,    13,    14,    15,    36,    55,     3,     9,
      16,    17,    18,    19,    20,    21,    22,    23,    24,    25,
      26,    27,    28,    29,    30,    31,    32,    33,    34,    63,
       3,     3,     3,     3,     3,     3,     3,    37,     3,     3,
       3,     3,    49,    39,     3,    11,    43,    35,    43,    64,
       9,     9,    62,     3,     3,     3,     3,    42,     3,     3,
       3,     3,    63,     3,    65,     3,     3,    63,    52,    53,
      38,    36,    43,    63,    63
};

#define yyerrok		(yyerrstatus = 0)
#define yyclearin	(yychar = YYEMPTY)
#define YYEMPTY		(-2)
#define YYEOF		0

#define YYACCEPT	goto yyacceptlab
#define YYABORT		goto yyabortlab
#define YYERROR		goto yyerrorlab


/* Like YYERROR except do call yyerror.  This remains here temporarily
   to ease the transition to the new meaning of YYERROR, for GCC.
   Once GCC version 2 has supplanted version 1, this can go.  However,
   YYFAIL appears to be in use.  Nevertheless, it is formally deprecated
   in Bison 2.4.2's NEWS entry, where a plan to phase it out is
   discussed.  */

#define YYFAIL		goto yyerrlab
#if defined YYFAIL
  /* This is here to suppress warnings from the GCC cpp's
     -Wunused-macros.  Normally we don't worry about that warning, but
     some users do, and we want to make it easy for users to remove
     YYFAIL uses, which will produce warnings from Bison 2.5.  */
#endif

#define YYRECOVERING()  (!!yyerrstatus)

#define YYBACKUP(Token, Value)                                  \
do                                                              \
  if (yychar == YYEMPTY)                                        \
    {                                                           \
      yychar = (Token);                                         \
      yylval = (Value);                                         \
      YYPOPSTACK (yylen);                                       \
      yystate = *yyssp;                                         \
      goto yybackup;                                            \
    }                                                           \
  else                                                          \
    {                                                           \
      yyerror (YY_("syntax error: cannot back up")); \
      YYERROR;							\
    }								\
while (YYID (0))

/* Error token number */
#define YYTERROR	1
#define YYERRCODE	256


/* This macro is provided for backward compatibility. */
#ifndef YY_LOCATION_PRINT
# define YY_LOCATION_PRINT(File, Loc) ((void) 0)
#endif


/* YYLEX -- calling `yylex' with the right arguments.  */
#ifdef YYLEX_PARAM
# define YYLEX yylex (YYLEX_PARAM)
#else
# define YYLEX yylex ()
#endif

/* Enable debugging if requested.  */
#if YYDEBUG

# ifndef YYFPRINTF
#  include <stdio.h> /* INFRINGES ON USER NAME SPACE */
#  define YYFPRINTF fprintf
# endif

# define YYDPRINTF(Args)			\
do {						\
  if (yydebug)					\
    YYFPRINTF Args;				\
} while (YYID (0))

# define YY_SYMBOL_PRINT(Title, Type, Value, Location)			  \
do {									  \
  if (yydebug)								  \
    {									  \
      YYFPRINTF (stderr, "%s ", Title);					  \
      yy_symbol_print (stderr,						  \
		  Type, Value); \
      YYFPRINTF (stderr, "\n");						  \
    }									  \
} while (YYID (0))


/*--------------------------------.
| Print this symbol on YYOUTPUT.  |
`--------------------------------*/

/*ARGSUSED*/
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static void
yy_symbol_value_print (FILE *yyoutput, int yytype, YYSTYPE const * const yyvaluep)
#else
static void
yy_symbol_value_print (yyoutput, yytype, yyvaluep)
    FILE *yyoutput;
    int yytype;
    YYSTYPE const * const yyvaluep;
#endif
{
  FILE *yyo = yyoutput;
  YYUSE (yyo);
  if (!yyvaluep)
    return;
# ifdef YYPRINT
  if (yytype < YYNTOKENS)
    YYPRINT (yyoutput, yytoknum[yytype], *yyvaluep);
# else
  YYUSE (yyoutput);
# endif
  switch (yytype)
    {
      default:
        break;
    }
}


/*--------------------------------.
| Print this symbol on YYOUTPUT.  |
`--------------------------------*/

#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static void
yy_symbol_print (FILE *yyoutput, int yytype, YYSTYPE const * const yyvaluep)
#else
static void
yy_symbol_print (yyoutput, yytype, yyvaluep)
    FILE *yyoutput;
    int yytype;
    YYSTYPE const * const yyvaluep;
#endif
{
  if (yytype < YYNTOKENS)
    YYFPRINTF (yyoutput, "token %s (", yytname[yytype]);
  else
    YYFPRINTF (yyoutput, "nterm %s (", yytname[yytype]);

  yy_symbol_value_print (yyoutput, yytype, yyvaluep);
  YYFPRINTF (yyoutput, ")");
}

/*------------------------------------------------------------------.
| yy_stack_print -- Print the state stack from its BOTTOM up to its |
| TOP (included).                                                   |
`------------------------------------------------------------------*/

#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static void
yy_stack_print (yytype_int16 *yybottom, yytype_int16 *yytop)
#else
static void
yy_stack_print (yybottom, yytop)
    yytype_int16 *yybottom;
    yytype_int16 *yytop;
#endif
{
  YYFPRINTF (stderr, "Stack now");
  for (; yybottom <= yytop; yybottom++)
    {
      int yybot = *yybottom;
      YYFPRINTF (stderr, " %d", yybot);
    }
  YYFPRINTF (stderr, "\n");
}

# define YY_STACK_PRINT(Bottom, Top)				\
do {								\
  if (yydebug)							\
    yy_stack_print ((Bottom), (Top));				\
} while (YYID (0))


/*------------------------------------------------.
| Report that the YYRULE is going to be reduced.  |
`------------------------------------------------*/

#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static void
yy_reduce_print (YYSTYPE *yyvsp, int yyrule)
#else
static void
yy_reduce_print (yyvsp, yyrule)
    YYSTYPE *yyvsp;
    int yyrule;
#endif
{
  int yynrhs = yyr2[yyrule];
  int yyi;
  unsigned long int yylno = yyrline[yyrule];
  YYFPRINTF (stderr, "Reducing stack by rule %d (line %lu):\n",
	     yyrule - 1, yylno);
  /* The symbols being reduced.  */
  for (yyi = 0; yyi < yynrhs; yyi++)
    {
      YYFPRINTF (stderr, "   $%d = ", yyi + 1);
      yy_symbol_print (stderr, yyrhs[yyprhs[yyrule] + yyi],
		       &(yyvsp[(yyi + 1) - (yynrhs)])
		       		       );
      YYFPRINTF (stderr, "\n");
    }
}

# define YY_REDUCE_PRINT(Rule)		\
do {					\
  if (yydebug)				\
    yy_reduce_print (yyvsp, Rule); \
} while (YYID (0))

/* Nonzero means print parse trace.  It is left uninitialized so that
   multiple parsers can coexist.  */
int yydebug;
#else /* !YYDEBUG */
# define YYDPRINTF(Args)
# define YY_SYMBOL_PRINT(Title, Type, Value, Location)
# define YY_STACK_PRINT(Bottom, Top)
# define YY_REDUCE_PRINT(Rule)
#endif /* !YYDEBUG */


/* YYINITDEPTH -- initial size of the parser's stacks.  */
#ifndef	YYINITDEPTH
# define YYINITDEPTH 200
#endif

/* YYMAXDEPTH -- maximum size the stacks can grow to (effective only
   if the built-in stack extension method is used).

   Do not make this value too large; the results are undefined if
   YYSTACK_ALLOC_MAXIMUM < YYSTACK_BYTES (YYMAXDEPTH)
   evaluated with infinite-precision integer arithmetic.  */

#ifndef YYMAXDEPTH
# define YYMAXDEPTH 10000
#endif


#if YYERROR_VERBOSE

# ifndef yystrlen
#  if defined __GLIBC__ && defined _STRING_H
#   define yystrlen strlen
#  else
/* Return the length of YYSTR.  */
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static YYSIZE_T
yystrlen (const char *yystr)
#else
static YYSIZE_T
yystrlen (yystr)
    const char *yystr;
#endif
{
  YYSIZE_T yylen;
  for (yylen = 0; yystr[yylen]; yylen++)
    continue;
  return yylen;
}
#  endif
# endif

# ifndef yystpcpy
#  if defined __GLIBC__ && defined _STRING_H && defined _GNU_SOURCE
#   define yystpcpy stpcpy
#  else
/* Copy YYSRC to YYDEST, returning the address of the terminating '\0' in
   YYDEST.  */
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static char *
yystpcpy (char *yydest, const char *yysrc)
#else
static char *
yystpcpy (yydest, yysrc)
    char *yydest;
    const char *yysrc;
#endif
{
  char *yyd = yydest;
  const char *yys = yysrc;

  while ((*yyd++ = *yys++) != '\0')
    continue;

  return yyd - 1;
}
#  endif
# endif

# ifndef yytnamerr
/* Copy to YYRES the contents of YYSTR after stripping away unnecessary
   quotes and backslashes, so that it's suitable for yyerror.  The
   heuristic is that double-quoting is unnecessary unless the string
   contains an apostrophe, a comma, or backslash (other than
   backslash-backslash).  YYSTR is taken from yytname.  If YYRES is
   null, do not copy; instead, return the length of what the result
   would have been.  */
static YYSIZE_T
yytnamerr (char *yyres, const char *yystr)
{
  if (*yystr == '"')
    {
      YYSIZE_T yyn = 0;
      char const *yyp = yystr;

      for (;;)
	switch (*++yyp)
	  {
	  case '\'':
	  case ',':
	    goto do_not_strip_quotes;

	  case '\\':
	    if (*++yyp != '\\')
	      goto do_not_strip_quotes;
	    /* Fall through.  */
	  default:
	    if (yyres)
	      yyres[yyn] = *yyp;
	    yyn++;
	    break;

	  case '"':
	    if (yyres)
	      yyres[yyn] = '\0';
	    return yyn;
	  }
    do_not_strip_quotes: ;
    }

  if (! yyres)
    return yystrlen (yystr);

  return yystpcpy (yyres, yystr) - yyres;
}
# endif

/* Copy into *YYMSG, which is of size *YYMSG_ALLOC, an error message
   about the unexpected token YYTOKEN for the state stack whose top is
   YYSSP.

   Return 0 if *YYMSG was successfully written.  Return 1 if *YYMSG is
   not large enough to hold the message.  In that case, also set
   *YYMSG_ALLOC to the required number of bytes.  Return 2 if the
   required number of bytes is too large to store.  */
static int
yysyntax_error (YYSIZE_T *yymsg_alloc, char **yymsg,
                yytype_int16 *yyssp, int yytoken)
{
  YYSIZE_T yysize0 = yytnamerr (YY_NULL, yytname[yytoken]);
  YYSIZE_T yysize = yysize0;
  enum { YYERROR_VERBOSE_ARGS_MAXIMUM = 5 };
  /* Internationalized format string. */
  const char *yyformat = YY_NULL;
  /* Arguments of yyformat. */
  char const *yyarg[YYERROR_VERBOSE_ARGS_MAXIMUM];
  /* Number of reported tokens (one for the "unexpected", one per
     "expected"). */
  int yycount = 0;

  /* There are many possibilities here to consider:
     - Assume YYFAIL is not used.  It's too flawed to consider.  See
       <http://lists.gnu.org/archive/html/bison-patches/2009-12/msg00024.html>
       for details.  YYERROR is fine as it does not invoke this
       function.
     - If this state is a consistent state with a default action, then
       the only way this function was invoked is if the default action
       is an error action.  In that case, don't check for expected
       tokens because there are none.
     - The only way there can be no lookahead present (in yychar) is if
       this state is a consistent state with a default action.  Thus,
       detecting the absence of a lookahead is sufficient to determine
       that there is no unexpected or expected token to report.  In that
       case, just report a simple "syntax error".
     - Don't assume there isn't a lookahead just because this state is a
       consistent state with a default action.  There might have been a
       previous inconsistent state, consistent state with a non-default
       action, or user semantic action that manipulated yychar.
     - Of course, the expected token list depends on states to have
       correct lookahead information, and it depends on the parser not
       to perform extra reductions after fetching a lookahead from the
       scanner and before detecting a syntax error.  Thus, state merging
       (from LALR or IELR) and default reductions corrupt the expected
       token list.  However, the list is correct for canonical LR with
       one exception: it will still contain any token that will not be
       accepted due to an error action in a later state.
  */
  if (yytoken != YYEMPTY)
    {
      int yyn = yypact[*yyssp];
      yyarg[yycount++] = yytname[yytoken];
      if (!yypact_value_is_default (yyn))
        {
          /* Start YYX at -YYN if negative to avoid negative indexes in
             YYCHECK.  In other words, skip the first -YYN actions for
             this state because they are default actions.  */
          int yyxbegin = yyn < 0 ? -yyn : 0;
          /* Stay within bounds of both yycheck and yytname.  */
          int yychecklim = YYLAST - yyn + 1;
          int yyxend = yychecklim < YYNTOKENS ? yychecklim : YYNTOKENS;
          int yyx;

          for (yyx = yyxbegin; yyx < yyxend; ++yyx)
            if (yycheck[yyx + yyn] == yyx && yyx != YYTERROR
                && !yytable_value_is_error (yytable[yyx + yyn]))
              {
                if (yycount == YYERROR_VERBOSE_ARGS_MAXIMUM)
                  {
                    yycount = 1;
                    yysize = yysize0;
                    break;
                  }
                yyarg[yycount++] = yytname[yyx];
                {
                  YYSIZE_T yysize1 = yysize + yytnamerr (YY_NULL, yytname[yyx]);
                  if (! (yysize <= yysize1
                         && yysize1 <= YYSTACK_ALLOC_MAXIMUM))
                    return 2;
                  yysize = yysize1;
                }
              }
        }
    }

  switch (yycount)
    {
# define YYCASE_(N, S)                      \
      case N:                               \
        yyformat = S;                       \
      break
      YYCASE_(0, YY_("syntax error"));
      YYCASE_(1, YY_("syntax error, unexpected %s"));
      YYCASE_(2, YY_("syntax error, unexpected %s, expecting %s"));
      YYCASE_(3, YY_("syntax error, unexpected %s, expecting %s or %s"));
      YYCASE_(4, YY_("syntax error, unexpected %s, expecting %s or %s or %s"));
      YYCASE_(5, YY_("syntax error, unexpected %s, expecting %s or %s or %s or %s"));
# undef YYCASE_
    }

  {
    YYSIZE_T yysize1 = yysize + yystrlen (yyformat);
    if (! (yysize <= yysize1 && yysize1 <= YYSTACK_ALLOC_MAXIMUM))
      return 2;
    yysize = yysize1;
  }

  if (*yymsg_alloc < yysize)
    {
      *yymsg_alloc = 2 * yysize;
      if (! (yysize <= *yymsg_alloc
             && *yymsg_alloc <= YYSTACK_ALLOC_MAXIMUM))
        *yymsg_alloc = YYSTACK_ALLOC_MAXIMUM;
      return 1;
    }

  /* Avoid sprintf, as that infringes on the user's name space.
     Don't have undefined behavior even if the translation
     produced a string with the wrong number of "%s"s.  */
  {
    char *yyp = *yymsg;
    int yyi = 0;
    while ((*yyp = *yyformat) != '\0')
      if (*yyp == '%' && yyformat[1] == 's' && yyi < yycount)
        {
          yyp += yytnamerr (yyp, yyarg[yyi++]);
          yyformat += 2;
        }
      else
        {
          yyp++;
          yyformat++;
        }
  }
  return 0;
}
#endif /* YYERROR_VERBOSE */

/*-----------------------------------------------.
| Release the memory associated to this symbol.  |
`-----------------------------------------------*/

/*ARGSUSED*/
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static void
yydestruct (const char *yymsg, int yytype, YYSTYPE *yyvaluep)
#else
static void
yydestruct (yymsg, yytype, yyvaluep)
    const char *yymsg;
    int yytype;
    YYSTYPE *yyvaluep;
#endif
{
  YYUSE (yyvaluep);

  if (!yymsg)
    yymsg = "Deleting";
  YY_SYMBOL_PRINT (yymsg, yytype, yyvaluep, yylocationp);

  switch (yytype)
    {

      default:
        break;
    }
}




/* The lookahead symbol.  */
int yychar;


#ifndef YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
# define YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
# define YY_IGNORE_MAYBE_UNINITIALIZED_END
#endif
#ifndef YY_INITIAL_VALUE
# define YY_INITIAL_VALUE(Value) /* Nothing. */
#endif

/* The semantic value of the lookahead symbol.  */
YYSTYPE yylval YY_INITIAL_VALUE(yyval_default);

/* Number of syntax errors so far.  */
int yynerrs;


/*----------.
| yyparse.  |
`----------*/

#ifdef YYPARSE_PARAM
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
int
yyparse (void *YYPARSE_PARAM)
#else
int
yyparse (YYPARSE_PARAM)
    void *YYPARSE_PARAM;
#endif
#else /* ! YYPARSE_PARAM */
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
int
yyparse (void)
#else
int
yyparse ()

#endif
#endif
{
    int yystate;
    /* Number of tokens to shift before error messages enabled.  */
    int yyerrstatus;

    /* The stacks and their tools:
       `yyss': related to states.
       `yyvs': related to semantic values.

       Refer to the stacks through separate pointers, to allow yyoverflow
       to reallocate them elsewhere.  */

    /* The state stack.  */
    yytype_int16 yyssa[YYINITDEPTH];
    yytype_int16 *yyss;
    yytype_int16 *yyssp;

    /* The semantic value stack.  */
    YYSTYPE yyvsa[YYINITDEPTH];
    YYSTYPE *yyvs;
    YYSTYPE *yyvsp;

    YYSIZE_T yystacksize;

  int yyn;
  int yyresult;
  /* Lookahead token as an internal (translated) token number.  */
  int yytoken = 0;
  /* The variables used to return semantic value and location from the
     action routines.  */
  YYSTYPE yyval;

#if YYERROR_VERBOSE
  /* Buffer for error messages, and its allocated size.  */
  char yymsgbuf[128];
  char *yymsg = yymsgbuf;
  YYSIZE_T yymsg_alloc = sizeof yymsgbuf;
#endif

#define YYPOPSTACK(N)   (yyvsp -= (N), yyssp -= (N))

  /* The number of symbols on the RHS of the reduced rule.
     Keep to zero when no symbol should be popped.  */
  int yylen = 0;

  yyssp = yyss = yyssa;
  yyvsp = yyvs = yyvsa;
  yystacksize = YYINITDEPTH;

  YYDPRINTF ((stderr, "Starting parse\n"));

  yystate = 0;
  yyerrstatus = 0;
  yynerrs = 0;
  yychar = YYEMPTY; /* Cause a token to be read.  */
  goto yysetstate;

/*------------------------------------------------------------.
| yynewstate -- Push a new state, which is found in yystate.  |
`------------------------------------------------------------*/
 yynewstate:
  /* In all cases, when you get here, the value and location stacks
     have just been pushed.  So pushing a state here evens the stacks.  */
  yyssp++;

 yysetstate:
  *yyssp = yystate;

  if (yyss + yystacksize - 1 <= yyssp)
    {
      /* Get the current used size of the three stacks, in elements.  */
      YYSIZE_T yysize = yyssp - yyss + 1;

#ifdef yyoverflow
      {
	/* Give user a chance to reallocate the stack.  Use copies of
	   these so that the &'s don't force the real ones into
	   memory.  */
	YYSTYPE *yyvs1 = yyvs;
	yytype_int16 *yyss1 = yyss;

	/* Each stack pointer address is followed by the size of the
	   data in use in that stack, in bytes.  This used to be a
	   conditional around just the two extra args, but that might
	   be undefined if yyoverflow is a macro.  */
	yyoverflow (YY_("memory exhausted"),
		    &yyss1, yysize * sizeof (*yyssp),
		    &yyvs1, yysize * sizeof (*yyvsp),
		    &yystacksize);

	yyss = yyss1;
	yyvs = yyvs1;
      }
#else /* no yyoverflow */
# ifndef YYSTACK_RELOCATE
      goto yyexhaustedlab;
# else
      /* Extend the stack our own way.  */
      if (YYMAXDEPTH <= yystacksize)
	goto yyexhaustedlab;
      yystacksize *= 2;
      if (YYMAXDEPTH < yystacksize)
	yystacksize = YYMAXDEPTH;

      {
	yytype_int16 *yyss1 = yyss;
	union yyalloc *yyptr =
	  (union yyalloc *) YYSTACK_ALLOC (YYSTACK_BYTES (yystacksize));
	if (! yyptr)
	  goto yyexhaustedlab;
	YYSTACK_RELOCATE (yyss_alloc, yyss);
	YYSTACK_RELOCATE (yyvs_alloc, yyvs);
#  undef YYSTACK_RELOCATE
	if (yyss1 != yyssa)
	  YYSTACK_FREE (yyss1);
      }
# endif
#endif /* no yyoverflow */

      yyssp = yyss + yysize - 1;
      yyvsp = yyvs + yysize - 1;

      YYDPRINTF ((stderr, "Stack size increased to %lu\n",
		  (unsigned long int) yystacksize));

      if (yyss + yystacksize - 1 <= yyssp)
	YYABORT;
    }

  YYDPRINTF ((stderr, "Entering state %d\n", yystate));

  if (yystate == YYFINAL)
    YYACCEPT;

  goto yybackup;

/*-----------.
| yybackup.  |
`-----------*/
yybackup:

  /* Do appropriate processing given the current state.  Read a
     lookahead token if we need one and don't already have one.  */

  /* First try to decide what to do without reference to lookahead token.  */
  yyn = yypact[yystate];
  if (yypact_value_is_default (yyn))
    goto yydefault;

  /* Not known => get a lookahead token if don't already have one.  */

  /* YYCHAR is either YYEMPTY or YYEOF or a valid lookahead symbol.  */
  if (yychar == YYEMPTY)
    {
      YYDPRINTF ((stderr, "Reading a token: "));
      yychar = YYLEX;
    }

  if (yychar <= YYEOF)
    {
      yychar = yytoken = YYEOF;
      YYDPRINTF ((stderr, "Now at end of input.\n"));
    }
  else
    {
      yytoken = YYTRANSLATE (yychar);
      YY_SYMBOL_PRINT ("Next token is", yytoken, &yylval, &yylloc);
    }

  /* If the proper action on seeing token YYTOKEN is to reduce or to
     detect an error, take that action.  */
  yyn += yytoken;
  if (yyn < 0 || YYLAST < yyn || yycheck[yyn] != yytoken)
    goto yydefault;
  yyn = yytable[yyn];
  if (yyn <= 0)
    {
      if (yytable_value_is_error (yyn))
        goto yyerrlab;
      yyn = -yyn;
      goto yyreduce;
    }

  /* Count tokens shifted since error; after three, turn off error
     status.  */
  if (yyerrstatus)
    yyerrstatus--;

  /* Shift the lookahead token.  */
  YY_SYMBOL_PRINT ("Shifting", yytoken, &yylval, &yylloc);

  /* Discard the shifted token.  */
  yychar = YYEMPTY;

  yystate = yyn;
  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  *++yyvsp = yylval;
  YY_IGNORE_MAYBE_UNINITIALIZED_END

  goto yynewstate;


/*-----------------------------------------------------------.
| yydefault -- do the default action for the current state.  |
`-----------------------------------------------------------*/
yydefault:
  yyn = yydefact[yystate];
  if (yyn == 0)
    goto yyerrlab;
  goto yyreduce;


/*-----------------------------.
| yyreduce -- Do a reduction.  |
`-----------------------------*/
yyreduce:
  /* yyn is the number of a rule to reduce with.  */
  yylen = yyr2[yyn];

  /* If YYLEN is nonzero, implement the default value of the action:
     `$$ = $1'.

     Otherwise, the following line sets YYVAL to garbage.
     This behavior is undocumented and Bison
     users should not rely upon it.  Assigning to YYVAL
     unconditionally makes the parser a bit smaller, and it avoids a
     GCC warning that YYVAL may be used uninitialized.  */
  yyval = yyvsp[1-yylen];


  YY_REDUCE_PRINT (yyn);
  switch (yyn)
    {
        case 2:
/* Line 1792 of yacc.c  */
#line 147 "pandatool/src/vrml/vrmlParser.yxx"
    {
  parsed_scene = (yyvsp[(1) - (1)].scene);
}
    break;

  case 3:
/* Line 1792 of yacc.c  */
#line 154 "pandatool/src/vrml/vrmlParser.yxx"
    {
  (yyval.scene) = new VrmlScene;
}
    break;

  case 4:
/* Line 1792 of yacc.c  */
#line 158 "pandatool/src/vrml/vrmlParser.yxx"
    {
  Declaration d;
  d._node = (yyvsp[(2) - (2)].nodeRef);
  (yyvsp[(1) - (2)].scene)->push_back(d);
  (yyval.scene) = (yyvsp[(1) - (2)].scene);
}
    break;

  case 7:
/* Line 1792 of yacc.c  */
#line 170 "pandatool/src/vrml/vrmlParser.yxx"
    {
  (yyval.nodeRef)._p = (yyvsp[(1) - (1)].node);
  (yyval.nodeRef)._type = SFNodeRef::T_unnamed;
  (yyval.nodeRef)._name = NULL;
}
    break;

  case 8:
/* Line 1792 of yacc.c  */
#line 176 "pandatool/src/vrml/vrmlParser.yxx"
    {
  (yyval.nodeRef)._p = (yyvsp[(3) - (3)].node);
  (yyval.nodeRef)._type = SFNodeRef::T_def;
  (yyval.nodeRef)._name = (yyvsp[(2) - (3)].string);
}
    break;

  case 9:
/* Line 1792 of yacc.c  */
#line 182 "pandatool/src/vrml/vrmlParser.yxx"
    {
  (yyval.nodeRef)._p = NULL;
  (yyval.nodeRef)._type = SFNodeRef::T_use;
  (yyval.nodeRef)._name = (yyvsp[(2) - (2)].string);
}
    break;

  case 12:
/* Line 1792 of yacc.c  */
#line 195 "pandatool/src/vrml/vrmlParser.yxx"
    { beginProto((yyvsp[(2) - (2)].string)); }
    break;

  case 13:
/* Line 1792 of yacc.c  */
#line 197 "pandatool/src/vrml/vrmlParser.yxx"
    { endProto();  free((yyvsp[(2) - (9)].string));}
    break;

  case 14:
/* Line 1792 of yacc.c  */
#line 201 "pandatool/src/vrml/vrmlParser.yxx"
    { beginProto((yyvsp[(2) - (2)].string)); }
    break;

  case 15:
/* Line 1792 of yacc.c  */
#line 203 "pandatool/src/vrml/vrmlParser.yxx"
    { expect(MFSTRING); }
    break;

  case 16:
/* Line 1792 of yacc.c  */
#line 204 "pandatool/src/vrml/vrmlParser.yxx"
    { endProto();  free((yyvsp[(2) - (8)].string)); }
    break;

  case 19:
/* Line 1792 of yacc.c  */
#line 212 "pandatool/src/vrml/vrmlParser.yxx"
    { addEventIn((yyvsp[(2) - (3)].string), (yyvsp[(3) - (3)].string));
                                              free((yyvsp[(2) - (3)].string)); free((yyvsp[(3) - (3)].string)); }
    break;

  case 20:
/* Line 1792 of yacc.c  */
#line 214 "pandatool/src/vrml/vrmlParser.yxx"
    { addEventOut((yyvsp[(2) - (3)].string), (yyvsp[(3) - (3)].string));
                                              free((yyvsp[(2) - (3)].string)); free((yyvsp[(3) - (3)].string)); }
    break;

  case 21:
/* Line 1792 of yacc.c  */
#line 217 "pandatool/src/vrml/vrmlParser.yxx"
    {
  int type = fieldType((yyvsp[(2) - (3)].string));
  expect(type); 
}
    break;

  case 22:
/* Line 1792 of yacc.c  */
#line 222 "pandatool/src/vrml/vrmlParser.yxx"
    {
  addField((yyvsp[(2) - (5)].string), (yyvsp[(3) - (5)].string), &((yyvsp[(5) - (5)].fv)));
  free((yyvsp[(2) - (5)].string)); 
  free((yyvsp[(3) - (5)].string)); 
}
    break;

  case 23:
/* Line 1792 of yacc.c  */
#line 228 "pandatool/src/vrml/vrmlParser.yxx"
    { 
  int type = fieldType((yyvsp[(2) - (3)].string));
  expect(type); 
}
    break;

  case 24:
/* Line 1792 of yacc.c  */
#line 233 "pandatool/src/vrml/vrmlParser.yxx"
    { 
  addExposedField((yyvsp[(2) - (5)].string), (yyvsp[(3) - (5)].string), &((yyvsp[(5) - (5)].fv)));
  free((yyvsp[(2) - (5)].string)); 
  free((yyvsp[(3) - (5)].string)); 
}
    break;

  case 27:
/* Line 1792 of yacc.c  */
#line 246 "pandatool/src/vrml/vrmlParser.yxx"
    { addEventIn((yyvsp[(2) - (3)].string), (yyvsp[(3) - (3)].string));
                                              free((yyvsp[(2) - (3)].string)); free((yyvsp[(3) - (3)].string)); }
    break;

  case 28:
/* Line 1792 of yacc.c  */
#line 248 "pandatool/src/vrml/vrmlParser.yxx"
    { addEventOut((yyvsp[(2) - (3)].string), (yyvsp[(3) - (3)].string));
                                              free((yyvsp[(2) - (3)].string)); free((yyvsp[(3) - (3)].string)); }
    break;

  case 29:
/* Line 1792 of yacc.c  */
#line 250 "pandatool/src/vrml/vrmlParser.yxx"
    { addField((yyvsp[(2) - (3)].string), (yyvsp[(3) - (3)].string));
                                              free((yyvsp[(2) - (3)].string)); free((yyvsp[(3) - (3)].string)); }
    break;

  case 30:
/* Line 1792 of yacc.c  */
#line 252 "pandatool/src/vrml/vrmlParser.yxx"
    { addExposedField((yyvsp[(2) - (3)].string), (yyvsp[(3) - (3)].string));
                                              free((yyvsp[(2) - (3)].string)); free((yyvsp[(3) - (3)].string)); }
    break;

  case 31:
/* Line 1792 of yacc.c  */
#line 258 "pandatool/src/vrml/vrmlParser.yxx"
    { free((yyvsp[(2) - (8)].string)); free((yyvsp[(4) - (8)].string)); free((yyvsp[(6) - (8)].string)); free((yyvsp[(8) - (8)].string)); }
    break;

  case 32:
/* Line 1792 of yacc.c  */
#line 262 "pandatool/src/vrml/vrmlParser.yxx"
    { enterNode((yyvsp[(1) - (1)].string)); }
    break;

  case 33:
/* Line 1792 of yacc.c  */
#line 263 "pandatool/src/vrml/vrmlParser.yxx"
    { (yyval.node) = exitNode(); free((yyvsp[(1) - (5)].string));}
    break;

  case 36:
/* Line 1792 of yacc.c  */
#line 272 "pandatool/src/vrml/vrmlParser.yxx"
    { enterField((yyvsp[(1) - (1)].string)); }
    break;

  case 37:
/* Line 1792 of yacc.c  */
#line 274 "pandatool/src/vrml/vrmlParser.yxx"
    {
  storeField((yyvsp[(3) - (3)].fv));
  exitField(); 
  free((yyvsp[(1) - (3)].string)); 
}
    break;

  case 40:
/* Line 1792 of yacc.c  */
#line 283 "pandatool/src/vrml/vrmlParser.yxx"
    { inScript(); free((yyvsp[(2) - (3)].string)); free((yyvsp[(3) - (3)].string)); }
    break;

  case 41:
/* Line 1792 of yacc.c  */
#line 284 "pandatool/src/vrml/vrmlParser.yxx"
    { inScript(); free((yyvsp[(2) - (3)].string)); free((yyvsp[(3) - (3)].string)); }
    break;

  case 42:
/* Line 1792 of yacc.c  */
#line 285 "pandatool/src/vrml/vrmlParser.yxx"
    { inScript(); 
                                              int type = fieldType((yyvsp[(2) - (3)].string));
                                              expect(type); }
    break;

  case 43:
/* Line 1792 of yacc.c  */
#line 288 "pandatool/src/vrml/vrmlParser.yxx"
    { free((yyvsp[(2) - (5)].string)); free((yyvsp[(3) - (5)].string)); }
    break;

  case 44:
/* Line 1792 of yacc.c  */
#line 290 "pandatool/src/vrml/vrmlParser.yxx"
    { inScript(); free((yyvsp[(2) - (5)].string)); free((yyvsp[(3) - (5)].string)); free((yyvsp[(5) - (5)].string)); }
    break;

  case 45:
/* Line 1792 of yacc.c  */
#line 292 "pandatool/src/vrml/vrmlParser.yxx"
    { inScript(); free((yyvsp[(2) - (5)].string)); free((yyvsp[(3) - (5)].string)); free((yyvsp[(5) - (5)].string)); }
    break;

  case 63:
/* Line 1792 of yacc.c  */
#line 314 "pandatool/src/vrml/vrmlParser.yxx"
    { (yyval.fv)._sfnode = (yyvsp[(2) - (2)].nodeRef); }
    break;

  case 64:
/* Line 1792 of yacc.c  */
#line 316 "pandatool/src/vrml/vrmlParser.yxx"
    { 
  (yyval.fv)._sfnode._p = NULL;
  (yyval.fv)._sfnode._type = SFNodeRef::T_null;
  (yyval.fv)._sfnode._name = NULL;
}
    break;

  case 65:
/* Line 1792 of yacc.c  */
#line 321 "pandatool/src/vrml/vrmlParser.yxx"
    { (yyval.fv)._mf = (yyvsp[(2) - (2)].mfarray); }
    break;

  case 66:
/* Line 1792 of yacc.c  */
#line 322 "pandatool/src/vrml/vrmlParser.yxx"
    { free((yyvsp[(2) - (2)].string)); }
    break;

  case 67:
/* Line 1792 of yacc.c  */
#line 327 "pandatool/src/vrml/vrmlParser.yxx"
    {
  (yyval.mfarray) = (yyvsp[(2) - (3)].mfarray); 
}
    break;

  case 68:
/* Line 1792 of yacc.c  */
#line 331 "pandatool/src/vrml/vrmlParser.yxx"
    {
  (yyval.mfarray) = new MFArray;
  VrmlFieldValue v;
  v._sfnode = (yyvsp[(1) - (1)].nodeRef);
  (yyval.mfarray)->push_back(v);
}
    break;

  case 69:
/* Line 1792 of yacc.c  */
#line 341 "pandatool/src/vrml/vrmlParser.yxx"
    {
  (yyval.mfarray) = new MFArray;
}
    break;

  case 70:
/* Line 1792 of yacc.c  */
#line 345 "pandatool/src/vrml/vrmlParser.yxx"
    {
  VrmlFieldValue v;
  v._sfnode = (yyvsp[(2) - (2)].nodeRef);
  (yyvsp[(1) - (2)].mfarray)->push_back(v);
  (yyval.mfarray) = (yyvsp[(1) - (2)].mfarray);
}
    break;


/* Line 1792 of yacc.c  */
#line 1925 "built/tmp/vrmlParser.yxx.c"
      default: break;
    }
  /* User semantic actions sometimes alter yychar, and that requires
     that yytoken be updated with the new translation.  We take the
     approach of translating immediately before every use of yytoken.
     One alternative is translating here after every semantic action,
     but that translation would be missed if the semantic action invokes
     YYABORT, YYACCEPT, or YYERROR immediately after altering yychar or
     if it invokes YYBACKUP.  In the case of YYABORT or YYACCEPT, an
     incorrect destructor might then be invoked immediately.  In the
     case of YYERROR or YYBACKUP, subsequent parser actions might lead
     to an incorrect destructor call or verbose syntax error message
     before the lookahead is translated.  */
  YY_SYMBOL_PRINT ("-> $$ =", yyr1[yyn], &yyval, &yyloc);

  YYPOPSTACK (yylen);
  yylen = 0;
  YY_STACK_PRINT (yyss, yyssp);

  *++yyvsp = yyval;

  /* Now `shift' the result of the reduction.  Determine what state
     that goes to, based on the state we popped back to and the rule
     number reduced by.  */

  yyn = yyr1[yyn];

  yystate = yypgoto[yyn - YYNTOKENS] + *yyssp;
  if (0 <= yystate && yystate <= YYLAST && yycheck[yystate] == *yyssp)
    yystate = yytable[yystate];
  else
    yystate = yydefgoto[yyn - YYNTOKENS];

  goto yynewstate;


/*------------------------------------.
| yyerrlab -- here on detecting error |
`------------------------------------*/
yyerrlab:
  /* Make sure we have latest lookahead translation.  See comments at
     user semantic actions for why this is necessary.  */
  yytoken = yychar == YYEMPTY ? YYEMPTY : YYTRANSLATE (yychar);

  /* If not already recovering from an error, report this error.  */
  if (!yyerrstatus)
    {
      ++yynerrs;
#if ! YYERROR_VERBOSE
      yyerror (YY_("syntax error"));
#else
# define YYSYNTAX_ERROR yysyntax_error (&yymsg_alloc, &yymsg, \
                                        yyssp, yytoken)
      {
        char const *yymsgp = YY_("syntax error");
        int yysyntax_error_status;
        yysyntax_error_status = YYSYNTAX_ERROR;
        if (yysyntax_error_status == 0)
          yymsgp = yymsg;
        else if (yysyntax_error_status == 1)
          {
            if (yymsg != yymsgbuf)
              YYSTACK_FREE (yymsg);
            yymsg = (char *) YYSTACK_ALLOC (yymsg_alloc);
            if (!yymsg)
              {
                yymsg = yymsgbuf;
                yymsg_alloc = sizeof yymsgbuf;
                yysyntax_error_status = 2;
              }
            else
              {
                yysyntax_error_status = YYSYNTAX_ERROR;
                yymsgp = yymsg;
              }
          }
        yyerror (yymsgp);
        if (yysyntax_error_status == 2)
          goto yyexhaustedlab;
      }
# undef YYSYNTAX_ERROR
#endif
    }



  if (yyerrstatus == 3)
    {
      /* If just tried and failed to reuse lookahead token after an
	 error, discard it.  */

      if (yychar <= YYEOF)
	{
	  /* Return failure if at end of input.  */
	  if (yychar == YYEOF)
	    YYABORT;
	}
      else
	{
	  yydestruct ("Error: discarding",
		      yytoken, &yylval);
	  yychar = YYEMPTY;
	}
    }

  /* Else will try to reuse lookahead token after shifting the error
     token.  */
  goto yyerrlab1;


/*---------------------------------------------------.
| yyerrorlab -- error raised explicitly by YYERROR.  |
`---------------------------------------------------*/
yyerrorlab:

  /* Pacify compilers like GCC when the user code never invokes
     YYERROR and the label yyerrorlab therefore never appears in user
     code.  */
  if (/*CONSTCOND*/ 0)
     goto yyerrorlab;

  /* Do not reclaim the symbols of the rule which action triggered
     this YYERROR.  */
  YYPOPSTACK (yylen);
  yylen = 0;
  YY_STACK_PRINT (yyss, yyssp);
  yystate = *yyssp;
  goto yyerrlab1;


/*-------------------------------------------------------------.
| yyerrlab1 -- common code for both syntax error and YYERROR.  |
`-------------------------------------------------------------*/
yyerrlab1:
  yyerrstatus = 3;	/* Each real token shifted decrements this.  */

  for (;;)
    {
      yyn = yypact[yystate];
      if (!yypact_value_is_default (yyn))
	{
	  yyn += YYTERROR;
	  if (0 <= yyn && yyn <= YYLAST && yycheck[yyn] == YYTERROR)
	    {
	      yyn = yytable[yyn];
	      if (0 < yyn)
		break;
	    }
	}

      /* Pop the current state because it cannot handle the error token.  */
      if (yyssp == yyss)
	YYABORT;


      yydestruct ("Error: popping",
		  yystos[yystate], yyvsp);
      YYPOPSTACK (1);
      yystate = *yyssp;
      YY_STACK_PRINT (yyss, yyssp);
    }

  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  *++yyvsp = yylval;
  YY_IGNORE_MAYBE_UNINITIALIZED_END


  /* Shift the error token.  */
  YY_SYMBOL_PRINT ("Shifting", yystos[yyn], yyvsp, yylsp);

  yystate = yyn;
  goto yynewstate;


/*-------------------------------------.
| yyacceptlab -- YYACCEPT comes here.  |
`-------------------------------------*/
yyacceptlab:
  yyresult = 0;
  goto yyreturn;

/*-----------------------------------.
| yyabortlab -- YYABORT comes here.  |
`-----------------------------------*/
yyabortlab:
  yyresult = 1;
  goto yyreturn;

#if !defined yyoverflow || YYERROR_VERBOSE
/*-------------------------------------------------.
| yyexhaustedlab -- memory exhaustion comes here.  |
`-------------------------------------------------*/
yyexhaustedlab:
  yyerror (YY_("memory exhausted"));
  yyresult = 2;
  /* Fall through.  */
#endif

yyreturn:
  if (yychar != YYEMPTY)
    {
      /* Make sure we have latest lookahead translation.  See comments at
         user semantic actions for why this is necessary.  */
      yytoken = YYTRANSLATE (yychar);
      yydestruct ("Cleanup: discarding lookahead",
                  yytoken, &yylval);
    }
  /* Do not reclaim the symbols of the rule which action triggered
     this YYABORT or YYACCEPT.  */
  YYPOPSTACK (yylen);
  YY_STACK_PRINT (yyss, yyssp);
  while (yyssp != yyss)
    {
      yydestruct ("Cleanup: popping",
		  yystos[*yyssp], yyvsp);
      YYPOPSTACK (1);
    }
#ifndef yyoverflow
  if (yyss != yyssa)
    YYSTACK_FREE (yyss);
#endif
#if YYERROR_VERBOSE
  if (yymsg != yymsgbuf)
    YYSTACK_FREE (yymsg);
#endif
  /* Make sure YYID is used.  */
  return YYID (yyresult);
}


/* Line 2055 of yacc.c  */
#line 353 "pandatool/src/vrml/vrmlParser.yxx"


static void
beginProto(const char *protoName)
{
    // Any protos in the implementation are in a local namespace:
    VrmlNodeType::pushNameSpace();

    VrmlNodeType *t = new VrmlNodeType(protoName);
    currentProtoStack.push(t);
}

static void
endProto()
{
    // Make any protos defined in implementation unavailable:
    VrmlNodeType::popNameSpace();

    // Add this proto definition:
    if (currentProtoStack.empty()) {
        cerr << "Error: Empty PROTO stack!\n";
    }
    else {
        VrmlNodeType *t = currentProtoStack.top();
        currentProtoStack.pop();
        VrmlNodeType::addToNameSpace(t);
    }
}

int
addField(const char *type, const char *name,
         const VrmlFieldValue *dflt)
{
    return add(&VrmlNodeType::addField, type, name, dflt);
}

int
addEventIn(const char *type, const char *name,
           const VrmlFieldValue *dflt)
{
    return add(&VrmlNodeType::addEventIn, type, name, dflt);
}
int
addEventOut(const char *type, const char *name,
            const VrmlFieldValue *dflt)
{
  return add(&VrmlNodeType::addEventOut, type, name, dflt);
}
int
addExposedField(const char *type, const char *name,
                const VrmlFieldValue *dflt)
{
    return add(&VrmlNodeType::addExposedField, type, name, dflt);
}

int
add(void (VrmlNodeType::*func)(const char *, int, const VrmlFieldValue *), 
    const char *typeString, const char *name,
    const VrmlFieldValue *dflt)
{
    int type = fieldType(typeString);

    if (type == 0) {
        cerr << "Error: invalid field type: " << type << "\n";
    }

    // Need to add support for Script nodes:
    // if (inScript) ... ???

    if (currentProtoStack.empty()) {
        cerr << "Error: declaration outside of prototype\n";
        return 0;
    }
    VrmlNodeType *t = currentProtoStack.top();
    (t->*func)(name, type, dflt);

    return type;
}

int
fieldType(const char *type)
{
    if (strcmp(type, "SFBool") == 0) return SFBOOL;
    if (strcmp(type, "SFColor") == 0) return SFCOLOR;
    if (strcmp(type, "SFFloat") == 0) return SFFLOAT;
    if (strcmp(type, "SFImage") == 0) return SFIMAGE;
    if (strcmp(type, "SFInt32") == 0) return SFINT32;
    if (strcmp(type, "SFNode") == 0) return SFNODE;
    if (strcmp(type, "SFRotation") == 0) return SFROTATION;
    if (strcmp(type, "SFString") == 0) return SFSTRING;
    if (strcmp(type, "SFTime") == 0) return SFTIME;
    if (strcmp(type, "SFVec2f") == 0) return SFVEC2F;
    if (strcmp(type, "SFVec3f") == 0) return SFVEC3F;
    if (strcmp(type, "MFColor") == 0) return MFCOLOR;
    if (strcmp(type, "MFFloat") == 0) return MFFLOAT;
    if (strcmp(type, "MFInt32") == 0) return MFINT32;
    if (strcmp(type, "MFNode") == 0) return MFNODE;
    if (strcmp(type, "MFRotation") == 0) return MFROTATION;
    if (strcmp(type, "MFString") == 0) return MFSTRING;
    if (strcmp(type, "MFVec2f") == 0) return MFVEC2F;
    if (strcmp(type, "MFVec3f") == 0) return MFVEC3F;

    cerr << "Illegal field type: " << type << "\n";

    return 0;
}

void
enterNode(const char *nodeType)
{
    const VrmlNodeType *t = VrmlNodeType::find(nodeType);
    if (t == NULL) {
        char tmp[1000];
        sprintf(tmp, "Unknown node type '%s'", nodeType);
        vrmlyyerror(tmp);
    }
    FieldRec *fr = new FieldRec;
    fr->nodeType = t;
    fr->fieldName = NULL;
    fr->typeRec = NULL;
    currentField.push(fr);

    VrmlNode *node = new VrmlNode(t);
    currentNode.push(node);
}

VrmlNode *
exitNode()
{
    FieldRec *fr = currentField.top();
    nassertr(fr != NULL, NULL);
    currentField.pop();

    VrmlNode *node = currentNode.top();
    nassertr(node != NULL, NULL);
    currentNode.pop();

    //    cerr << "Just defined node:\n" << *node << "\n\n";

    delete fr;
    return node;
}

void
inScript()
{
    FieldRec *fr = currentField.top();
    if (fr->nodeType == NULL ||
        strcmp(fr->nodeType->getName(), "Script") != 0) {
        vrmlyyerror("interface declaration outside of Script or prototype");
    }
}

void
enterField(const char *fieldName)
{
    FieldRec *fr = currentField.top();
    nassertv(fr != NULL);

    fr->fieldName = fieldName;
    fr->typeRec = NULL;
    if (fr->nodeType != NULL) {
        // enterField is called when parsing eventIn and eventOut IS
        // declarations, in which case we don't need to do anything special--
        // the IS IDENTIFIER will be returned from the lexer normally.
        if (fr->nodeType->hasEventIn(fieldName) ||
            fr->nodeType->hasEventOut(fieldName))
            return;
    
        const VrmlNodeType::NameTypeRec *typeRec =
          fr->nodeType->hasField(fieldName);
        if (typeRec != NULL) {
            fr->typeRec = typeRec;
            // Let the lexer know what field type to expect:
            expect(typeRec->type);
        }
        else {
            cerr << "Error: Nodes of type " << fr->nodeType->getName() <<
                " do not have fields/eventIn/eventOut named " <<
                fieldName << "\n";
            // expect(ANY_FIELD);
        }
    }
    // else expect(ANY_FIELD);
}

void
storeField(const VrmlFieldValue &value) {
  FieldRec *fr = currentField.top();
  nassertv(fr != NULL);

  VrmlNode *node = currentNode.top();
  nassertv(node != NULL);

  if (fr->typeRec != NULL) {
    node->_fields.push_back(VrmlNode::Field(fr->typeRec, value));
  }
}

void
exitField()
{
    FieldRec *fr = currentField.top();
    nassertv(fr != NULL);

    fr->fieldName = NULL;
    fr->typeRec = NULL;
}

void
expect(int type)
{
    expectToken = type;
}

